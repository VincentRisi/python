/// ------------------------------------------------------------------
/// Copyright (c) 1996, 2004 Vincent Risi in Association 
///                          with Barone Budge and Dominick 
/// All rights reserved. 
/// This program and the accompanying materials are made available 
/// under the terms of the Common Public License v1.0 
/// which accompanies this distribution and is available at 
/// http://www.eclipse.org/legal/cpl-v10.html 
/// Contributors:
///    Vincent Risi
/// ------------------------------------------------------------------
/// System : JPortal
/// $Date: 2004/10/18 13:45:47 $
/// $Revision: 411.1 $ // YMM.Revision
/// ------------------------------------------------------------------
package vlab.jportal

import java.io.DataInputStream
import java.io.DataOutputStream
import java.io.IOException
import java.io.Serializable
import java.util.*

class Const : Serializable {
    @JvmField
    var name = ""

    @JvmField
    var values: Vector<Value>

    @Throws(IOException::class)
    fun reader(ids: DataInputStream) {
        name = ids.readUTF()
        val noOf = ids.readInt()
        for (i in 0 until noOf) {
            val v = Value()
            v.reader(ids)
            values.addElement(v)
        }
    }

    @Throws(IOException::class)
    fun writer(ods: DataOutputStream) {
        ods.writeUTF(name)
        ods.writeInt(values.size)
        for (i in values.indices) {
            val v = values.elementAt(i)
            v.writer(ods)
        }
    }

    companion object {
        private const val serialVersionUID = 1L
    }

    init {
        values = Vector()
    }
}