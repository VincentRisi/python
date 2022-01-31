// Copyright 2000-2022 JetBrains s.r.o. and other contributors. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.

package org.intellij.sdk.language.psi;

import com.intellij.psi.tree.IElementType;
import org.intellij.sdk.language.Idl2Language;
import org.jetbrains.annotations.NonNls;
import org.jetbrains.annotations.NotNull;

public class Idl2ElementType extends IElementType {

  public Idl2ElementType(@NotNull @NonNls String debugName) {
    super(debugName, Idl2Language.INSTANCE);
  }

}
