// Copyright 2000-2022 JetBrains s.r.o. and other contributors. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.

package org.intellij.sdk.language;

import com.intellij.openapi.fileTypes.LanguageFileType;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import javax.swing.*;

public class Idl2FileType extends LanguageFileType {

  public static final Idl2FileType INSTANCE = new Idl2FileType();

  private Idl2FileType() {
    super(Idl2Language.INSTANCE);
  }

  @NotNull
  @Override
  public String getName() {
    return "Idl2 File";
  }

  @NotNull
  @Override
  public String getDescription() {
    return "Idl2 language file";
  }

  @NotNull
  @Override
  public String getDefaultExtension() {
    return "idl2";
  }

  @Nullable
  @Override
  public Icon getIcon() {
    return Idl2Icons.FILE;
  }

}
