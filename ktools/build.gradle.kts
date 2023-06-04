import org.jetbrains.kotlin.gradle.tasks.KotlinCompile
import org.gradle.kotlin.dsl.withType as withType1

plugins {
    kotlin("jvm") version "1.7.10"
}

group = "me.vince"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies { testImplementation(kotlin("test")) }

tasks.test {
    useJUnit()
}
tasks.withType1<KotlinCompile>() {
    kotlinOptions.jvmTarget = "1.8"
}