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
package vlab.jportal

import java.io.Serializable

class Sequence : Serializable
{
    var name = ""
    var minValue = 0
    var maxValue = 999999999
    var increment = 1
    var cycleFlag = true
    var orderFlag = true
    var startWith = 1

    /**
     * Code starts at line
     */
    var start = 0

    companion object
    {
        /**
         *
         */
        private const val serialVersionUID = 1L
    }
}