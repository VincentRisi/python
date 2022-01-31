// Copyright 2000-2022 JetBrains s.r.o. and other contributors. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.

package org.intellij.sdk.language;

import com.intellij.openapi.editor.colors.TextAttributesKey;
import com.intellij.openapi.fileTypes.SyntaxHighlighter;
import com.intellij.openapi.options.colors.AttributesDescriptor;
import com.intellij.openapi.options.colors.ColorDescriptor;
import com.intellij.openapi.options.colors.ColorSettingsPage;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import javax.swing.*;
import java.util.Map;

public class Idl2ColorSettingsPage implements ColorSettingsPage {

  private static final AttributesDescriptor[] DESCRIPTORS = new AttributesDescriptor[]{
          new AttributesDescriptor("Key", Idl2SyntaxHighlighter.KEY),
          new AttributesDescriptor("Separator", Idl2SyntaxHighlighter.SEPARATOR),
          new AttributesDescriptor("Value", Idl2SyntaxHighlighter.VALUE),
          new AttributesDescriptor("Bad value", Idl2SyntaxHighlighter.BAD_CHARACTER)
  };

  @Nullable
  @Override
  public Icon getIcon() {
    return Idl2Icons.FILE;
  }

  @NotNull
  @Override
  public SyntaxHighlighter getHighlighter() {
    return new Idl2SyntaxHighlighter();
  }

  @NotNull
  @Override
  public String getDemoText() {
    return 
           "module Accuity;" +
           "version \"19.07.13.0\";" +
           "" +
           "code" +
           "BOTH:using namespace std;" +
           "#include \"date.h\"" +
           "#include \"xmlrecord.h\"" +
           "#include \"putty3shell.h\"" +
           "endcode" +
           "" +
           "message" +
           "{" +
           "  DB_ERROR        \"DB Exception Error.\"" +
           "  XCEPT_ERROR     \"Generic Exception Error.\"" +
           "  SCRIPT_ERROR    \"Script Error.\"" +
           "  PYTHON_ERROR    \"Python Exception Error.\"" +
           "  NOT_YET_DONE    \"This has not yet been done.\"" +
           "}" +
           "" +
           "private struct Accuity" +
           "{" +
           "  TBChar errors;" +
           "  Putty3Shell *putty3;" +
           "  char binFileName[256];" +
           "  char connectString[64];" +
           "code" +
           "  Connect.CB()->isVB = 0;" +
           "  LoadConfig();" +
           "  putty3 = new Putty3Shell(\"AccuityServer\", ConfigFile, \"ACCUITY\");" +
           "  runPython = putty3Runner;" +
           "onshutdown:" +
           "  delete putty3;" +
           "endcode" +
           "}";
  }

  @Nullable
  @Override
  public Map<String, TextAttributesKey> getAdditionalHighlightingTagToDescriptorMap() {
    return null;
  }

  @Override
  public AttributesDescriptor @NotNull [] getAttributeDescriptors() {
    return DESCRIPTORS;
  }

  @Override
  public ColorDescriptor @NotNull [] getColorDescriptors() {
    return ColorDescriptor.EMPTY_ARRAY;
  }

  @NotNull
  @Override
  public String getDisplayName() {
    return "Idl2";
  }

}
