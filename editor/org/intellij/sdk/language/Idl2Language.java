// Copyright 2000-2022 JetBrains s.r.o. and other contributors. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.

package org.intellij.sdk.language;

import com.intellij.lang.Language;

public class Idl2Language extends Language {

  public static final Idl2Language INSTANCE = new Idl2Language();

  private Idl2Language() {
    super("Idl2");
  }

}
