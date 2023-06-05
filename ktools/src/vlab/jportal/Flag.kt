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

/**
 * @author vince
 */
class Flag(var name: String, var value: Any, var description: String) : Serializable {
    companion object {
        /**
         *
         */
        private const val serialVersionUID = 1L
    }
}