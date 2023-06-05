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
 * This holds the field definition. It also supplies methods for the
 * Java format and various SQL formats.
 */
class Enumerator
/**
 * constructor ensures fields have correct default values
 */
    : Serializable {
    @JvmField
    var name = ""

    @JvmField
    var value = 0

    @Throws(IOException::class)
    fun reader(ids: DataInputStream) {
        name = ids.readUTF()
        value = ids.readInt()
    }

    @Throws(IOException::class)
    fun writer(ods: DataOutputStream) {
        ods.writeUTF(name)
        ods.writeInt(value)
    }

    companion object {
        private const val serialVersionUID = 1L
    }
}