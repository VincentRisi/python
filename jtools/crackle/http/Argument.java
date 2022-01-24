/// ------------------------------------------------------------------
/// Copyright (c) from 1996 Vincent Risi 
///
/// All rights reserved. 
/// This program and the accompanying materials are made available 
/// under the terms of the Common Public License v1.0 
/// which accompanies this distribution and is available at 
/// http://www.eclipse.org/legal/cpl-v10.html 
/// Contributors:
///    Vincent Risi
/// ------------------------------------------------------------------

package jtools.crackle.http;

import jtools.crackle.Field;

public class Argument
{
  public String useAs;
  public Field field;

  public Argument(Field field, String useAs)
  {
    this.field = field;
    this.useAs = useAs;
  }
}
