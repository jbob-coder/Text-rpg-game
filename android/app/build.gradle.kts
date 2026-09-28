plugins {
    id("com.android.application")
    id("com.chaquo.python")
}

android {
    namespace = "com.jbobcoder.textrpg"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.jbobcoder.textrpg"
        minSdk = 24
        targetSdk = 36
        versionCode = 1
        versionName = "0.1.0"

        ndk {
            abiFilters += listOf("armeabi-v7a", "arm64-v8a", "x86_64")
        }
    }

    sourceSets.getByName("main") {
        assets.srcDir("../../content")
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
}

chaquopy {
    defaultConfig {
        version = "3.11"
        pyc {
            src = false
        }
    }

    sourceSets {
        getByName("main") {
            srcDir("src/main/python")
            srcDir("../../src")
        }
    }
}
