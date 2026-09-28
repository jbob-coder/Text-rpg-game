package com.jbobcoder.textrpg;

import android.app.Activity;
import android.graphics.Color;
import android.graphics.Typeface;
import android.graphics.drawable.GradientDrawable;
import android.os.Bundle;
import android.util.AtomicFile;
import android.util.Log;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.nio.charset.StandardCharsets;
import java.util.Locale;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public final class MainActivity extends Activity {
    private static final String TAG = "TextRpgStartup";
    private static final String CONTENT_ASSET = "vertical_slice_01.json";
    private static final String SAVE_FILE = "save_v1.json";

    private static final int COLOR_BG = Color.rgb(24, 25, 30);
    private static final int COLOR_PANEL = Color.rgb(42, 44, 52);
    private static final int COLOR_TEXT = Color.rgb(239, 232, 211);
    private static final int COLOR_MUTED = Color.rgb(183, 176, 158);
    private static final int COLOR_ACCENT = Color.rgb(205, 170, 91);
    private static final int COLOR_DANGER = Color.rgb(180, 72, 72);

    private final ExecutorService gameExecutor = Executors.newSingleThreadExecutor();
    private volatile PyObject gameSession;
    private AtomicFile saveFile;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        saveFile = new AtomicFile(new File(getFilesDir(), SAVE_FILE));
        setContentView(buildMessageView(
                "THE GAME",
                "Starting local rules engine…",
                "If startup fails, this screen will be replaced by a visible diagnostic instead of remaining blank."
        ));
        gameExecutor.execute(this::initializeGame);
    }

    private void initializeGame() {
        try {
            Log.i(TAG, "Android bootstrap started");
            if (!Python.isStarted()) {
                AndroidPlatform platform = new AndroidPlatform(getApplication());
                platform.redirectStdioToLogcat();
                Python.start(platform);
            }
            Log.i(TAG, "Python runtime started");

            String contentJson = readAssetText(CONTENT_ASSET);
            String saveJson = readSaveIfPresent();

            Python python = Python.getInstance();
            PyObject bridge = python.getModule("android_bridge");
            gameSession = bridge.callAttr("create_session", contentJson, saveJson);

            String viewJson = gameSession.callAttr("view_json").toString();
            Log.i(TAG, "Rules engine session initialized");
            runOnUiThread(() -> renderView(viewJson));
        } catch (Throwable error) {
            showFailure("Startup failed", error);
        }
    }

    private void submitChoice(String choiceId) {
        if (gameSession == null) {
            showFailure("Choice failed", new IllegalStateException("Game session is not initialized"));
            return;
        }

        setContentView(buildMessageView(
                "THE GAME",
                "Resolving choice…",
                "Applying the choice through the authoritative local rules engine."
        ));

        gameExecutor.execute(() -> {
            try {
                String resultJson = gameSession.callAttr("choose_json", choiceId).toString();
                JSONObject result = new JSONObject(resultJson);
                String saveJson = result.getString("save");
                writeSaveAtomically(saveJson);
                String viewJson = result.getJSONObject("view").toString();

                Log.i(TAG, "Choice resolved and save committed: " + choiceId);
                runOnUiThread(() -> renderView(viewJson));
            } catch (Throwable error) {
                showFailure("Choice failed", error);
            }
        });
    }

    private void renderView(String viewJson) {
        try {
            JSONObject view = new JSONObject(viewJson);
            JSONObject game = view.getJSONObject("game");
            JSONObject scene = view.getJSONObject("scene");
            JSONObject status = view.getJSONObject("status");

            ScrollView scroll = new ScrollView(this);
            scroll.setFillViewport(true);
            scroll.setBackgroundColor(COLOR_BG);

            LinearLayout column = new LinearLayout(this);
            column.setOrientation(LinearLayout.VERTICAL);
            column.setPadding(dp(20), dp(20), dp(20), dp(28));
            scroll.addView(column, new ScrollView.LayoutParams(
                    ScrollView.LayoutParams.MATCH_PARENT,
                    ScrollView.LayoutParams.WRAP_CONTENT
            ));

            column.addView(text(
                    game.optString("title", "THE GAME"),
                    13,
                    COLOR_ACCENT,
                    Typeface.BOLD
            ));

            addWithTopMargin(
                    column,
                    text(
                            "Turn " + view.optInt("turn", 0)
                                    + "  •  " + formatMinutes(view.optInt("time_minutes", 0)),
                            13,
                            COLOR_MUTED,
                            Typeface.NORMAL
                    ),
                    4
            );

            JSONObject identity = status.optJSONObject("identity");
            String identityLine = buildIdentityLine(identity);
            if (!identityLine.isEmpty()) {
                addWithTopMargin(
                        column,
                        text(identityLine, 15, COLOR_TEXT, Typeface.BOLD),
                        14
                );
            }

            String resources = buildResourceLine(status.optJSONArray("resources"));
            if (!resources.isEmpty()) {
                addWithTopMargin(
                        column,
                        text(resources, 13, COLOR_MUTED, Typeface.NORMAL),
                        4
                );
            }

            View divider = new View(this);
            divider.setBackgroundColor(COLOR_ACCENT);
            LinearLayout.LayoutParams dividerParams = new LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT,
                    dp(2)
            );
            dividerParams.topMargin = dp(18);
            dividerParams.bottomMargin = dp(18);
            column.addView(divider, dividerParams);

            column.addView(text(
                    scene.optString("title", scene.optString("id", "Scene")),
                    26,
                    COLOR_TEXT,
                    Typeface.BOLD
            ));

            TextView body = text(
                    scene.optString("body", ""),
                    19,
                    COLOR_TEXT,
                    Typeface.NORMAL
            );
            body.setLineSpacing(0f, 1.18f);
            addWithTopMargin(column, body, 12);

            addWithTopMargin(
                    column,
                    text("DECISIONS", 13, COLOR_ACCENT, Typeface.BOLD),
                    24
            );

            JSONArray choices = scene.optJSONArray("choices");
            if (choices == null || choices.length() == 0) {
                addWithTopMargin(
                        column,
                        text(
                                "No choices are currently available.",
                                16,
                                COLOR_MUTED,
                                Typeface.ITALIC
                        ),
                        10
                );
            } else {
                for (int i = 0; i < choices.length(); i++) {
                    JSONObject choice = choices.getJSONObject(i);
                    String choiceId = choice.getString("id");
                    boolean enabled = choice.optBoolean("enabled", true);
                    String label = choice.optString("text", choiceId);
                    if (!enabled) {
                        label += "\nLocked: " + choice.optString(
                                "disabled_reason",
                                "Requirements not met"
                        );
                    }

                    Button button = new Button(this);
                    button.setAllCaps(false);
                    button.setGravity(Gravity.START | Gravity.CENTER_VERTICAL);
                    button.setText(label);
                    button.setTextSize(17);
                    button.setTextColor(enabled ? COLOR_TEXT : COLOR_MUTED);
                    button.setPadding(dp(16), dp(12), dp(16), dp(12));
                    button.setMinHeight(dp(58));
                    button.setStateListAnimator(null);
                    button.setEnabled(enabled);
                    button.setBackground(buildChoiceBackground(enabled));
                    if (enabled) {
                        button.setOnClickListener(v -> submitChoice(choiceId));
                    }

                    LinearLayout.LayoutParams buttonParams = new LinearLayout.LayoutParams(
                            LinearLayout.LayoutParams.MATCH_PARENT,
                            LinearLayout.LayoutParams.WRAP_CONTENT
                    );
                    buttonParams.topMargin = dp(10);
                    column.addView(button, buttonParams);
                }
            }

            addWithTopMargin(
                    column,
                    text(
                            "P0 Android bootstrap • local engine • autosave enabled",
                            11,
                            COLOR_MUTED,
                            Typeface.NORMAL
                    ),
                    28
            );

            setContentView(scroll);
        } catch (Throwable error) {
            showFailure("Render failed", error);
        }
    }

    private GradientDrawable buildChoiceBackground(boolean enabled) {
        GradientDrawable background = new GradientDrawable();
        background.setShape(GradientDrawable.RECTANGLE);
        background.setCornerRadius(0f);
        background.setColor(COLOR_PANEL);
        background.setStroke(dp(2), enabled ? COLOR_ACCENT : Color.rgb(95, 95, 100));
        return background;
    }

    private View buildMessageView(String title, String headline, String detail) {
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setGravity(Gravity.CENTER_VERTICAL);
        root.setPadding(dp(24), dp(24), dp(24), dp(24));
        root.setBackgroundColor(COLOR_BG);

        root.addView(text(title, 15, COLOR_ACCENT, Typeface.BOLD));
        addWithTopMargin(root, text(headline, 25, COLOR_TEXT, Typeface.BOLD), 12);
        addWithTopMargin(root, text(detail, 16, COLOR_MUTED, Typeface.NORMAL), 10);
        return root;
    }

    private void showFailure(String headline, Throwable error) {
        Log.e(TAG, headline, error);
        StringWriter writer = new StringWriter();
        error.printStackTrace(new PrintWriter(writer));
        String trace = writer.toString();
        if (trace.length() > 5000) {
            trace = trace.substring(0, 5000) + "\n…truncated…";
        }
        final String diagnostic = trace;

        runOnUiThread(() -> {
            ScrollView scroll = new ScrollView(this);
            scroll.setBackgroundColor(COLOR_BG);
            LinearLayout column = new LinearLayout(this);
            column.setOrientation(LinearLayout.VERTICAL);
            column.setPadding(dp(20), dp(20), dp(20), dp(28));
            scroll.addView(column);

            column.addView(text("THE GAME", 14, COLOR_ACCENT, Typeface.BOLD));
            addWithTopMargin(column, text(headline, 26, COLOR_DANGER, Typeface.BOLD), 12);
            addWithTopMargin(
                    column,
                    text(
                            "The app stopped safely. Existing save data was not deleted. "
                                    + "Use Logcat tag " + TAG + " for the full startup evidence.",
                            16,
                            COLOR_TEXT,
                            Typeface.NORMAL
                    ),
                    10
            );
            TextView traceView = text(diagnostic, 11, COLOR_MUTED, Typeface.NORMAL);
            traceView.setTextIsSelectable(true);
            addWithTopMargin(column, traceView, 16);
            setContentView(scroll);
        });
    }

    private TextView text(String value, int sp, int color, int style) {
        TextView view = new TextView(this);
        view.setText(value);
        view.setTextSize(sp);
        view.setTextColor(color);
        view.setTypeface(Typeface.create(Typeface.MONOSPACE, style));
        return view;
    }

    private void addWithTopMargin(LinearLayout parent, View child, int topDp) {
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
        );
        params.topMargin = dp(topDp);
        parent.addView(child, params);
    }

    private String buildIdentityLine(JSONObject identity) {
        if (identity == null) {
            return "";
        }
        String name = identity.optString("name", "");
        Object level = identity.opt("level");
        if (name.isEmpty() && level == null) {
            return "";
        }
        if (level != null && level != JSONObject.NULL) {
            return name.isEmpty() ? "Level " + level : name + "  •  Level " + level;
        }
        return name;
    }

    private String buildResourceLine(JSONArray resources) throws Exception {
        if (resources == null || resources.length() == 0) {
            return "";
        }
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < resources.length(); i++) {
            JSONObject resource = resources.getJSONObject(i);
            if (i > 0) {
                output.append("  •  ");
            }
            output.append(resource.optString("name", resource.optString("id", "Resource")));
            output.append(' ');
            output.append(formatNumber(resource.optDouble("current", 0)));
            output.append('/');
            output.append(formatNumber(resource.optDouble("max", 0)));
        }
        return output.toString();
    }

    private String formatNumber(double value) {
        double rounded = Math.rint(value);
        if (Math.abs(value - rounded) < 0.00001) {
            return Long.toString((long) rounded);
        }
        return String.format(Locale.US, "%.1f", value);
    }

    private String formatMinutes(int minutes) {
        int days = minutes / (24 * 60);
        int remainder = minutes % (24 * 60);
        int hours = remainder / 60;
        int mins = remainder % 60;
        if (days > 0) {
            return days + "d " + hours + "h " + mins + "m";
        }
        if (hours > 0) {
            return hours + "h " + mins + "m";
        }
        return mins + "m";
    }

    private String readAssetText(String name) throws Exception {
        try (InputStream input = getAssets().open(name);
             BufferedReader reader = new BufferedReader(
                     new InputStreamReader(input, StandardCharsets.UTF_8))) {
            StringBuilder output = new StringBuilder();
            char[] buffer = new char[4096];
            int count;
            while ((count = reader.read(buffer)) != -1) {
                output.append(buffer, 0, count);
            }
            return output.toString();
        }
    }

    private String readSaveIfPresent() throws Exception {
        try (FileInputStream input = saveFile.openRead();
             ByteArrayOutputStream output = new ByteArrayOutputStream()) {
            byte[] buffer = new byte[4096];
            int count;
            while ((count = input.read(buffer)) != -1) {
                output.write(buffer, 0, count);
            }
            return output.toString(StandardCharsets.UTF_8.name());
        } catch (FileNotFoundException missing) {
            return "";
        }
    }

    private void writeSaveAtomically(String saveJson) throws Exception {
        FileOutputStream output = null;
        try {
            output = saveFile.startWrite();
            OutputStreamWriter writer = new OutputStreamWriter(output, StandardCharsets.UTF_8);
            writer.write(saveJson);
            writer.flush();
            saveFile.finishWrite(output);
        } catch (Exception error) {
            if (output != null) {
                saveFile.failWrite(output);
            }
            throw error;
        }
    }

    private int dp(int value) {
        float density = getResources().getDisplayMetrics().density;
        return Math.round(value * density);
    }

    @Override
    protected void onDestroy() {
        gameExecutor.shutdownNow();
        super.onDestroy();
    }
}
