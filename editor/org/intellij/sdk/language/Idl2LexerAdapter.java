// Copyright 2000-2022 JetBrains s.r.o. and other contributors. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.

package org.intellij.sdk.language;

import com.intellij.lexer.FlexAdapter;

public class Idl2LexerAdapter extends FlexAdapter {

  public Idl2LexerAdapter() {
    super(new Idl2Lexer(null));
  }

}
