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

class Value : Serializable
{
    @JvmField
    var key = ""
    @JvmField
    var value = ""
    @Throws(IOException::class)
    fun reader(ids: DataInputStream)
    {
        key = ids.readUTF()
        value = ids.readUTF()
    }

    @Throws(IOException::class)
    fun writer(ods: DataOutputStream)
    {
        ods.writeUTF(key)
        ods.writeUTF(value)
    }

    companion object
    {
        private const val serialVersionUID = 1L
    }
}