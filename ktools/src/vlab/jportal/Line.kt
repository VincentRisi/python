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

import java.io.IOException
import java.io.DataInputStream
import java.io.DataOutputStream
import java.io.Serializable

/**
 * Lines of SQL Code
 */
class Line : Serializable
{
    @JvmField
    var line: String
    @JvmField
    var isVar: Boolean

    /**
     * Constructs line needed to be enclosed in double quotes
     */
    constructor(l: String)
    {
        line = l
        isVar = false
    }

    /**
     * Constructs line used in variable substitution
     */
    constructor(l: String, t: Boolean)
    {
        line = l
        isVar = t
    }

    @Throws(IOException::class)
    fun reader(ids: DataInputStream)
    {
        line = ids.readUTF()
        isVar = ids.readBoolean()
    }

    @Throws(IOException::class)
    fun writer(ods: DataOutputStream)
    {
        ods.writeUTF(line)
        ods.writeBoolean(isVar)
    }

    companion object
    {
        private const val serialVersionUID = 1L
    }
}