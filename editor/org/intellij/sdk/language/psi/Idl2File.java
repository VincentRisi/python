// Copyright 2000-2022 JetBrains s.r.o. and other contributors. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.

package org.intellij.sdk.language.psi;

import com.intellij.extapi.psi.PsiFileBase;
import com.intellij.openapi.fileTypes.FileType;
import com.intellij.psi.FileViewProvider;
import org.intellij.sdk.language.Idl2FileType;
import org.intellij.sdk.language.Idl2Language;
import org.jetbrains.annotations.NotNull;

public class Idl2File extends PsiFileBase {

  public Idl2File(@NotNull FileViewProvider viewProvider) {
    super(viewProvider, Idl2Language.INSTANCE);
  }

  @NotNull
  @Override
  public FileType getFileType() {
    return Idl2FileType.INSTANCE;
  }

  @Override
  public String toString() {
    return "Idl2 File";
  }

}
