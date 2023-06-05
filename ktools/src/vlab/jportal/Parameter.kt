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

import java.io.DataInputStream
import java.io.DataOutputStream
import java.io.IOException
import java.io.Serializable
import java.util.*

class Parameter : Serializable {
    var table: Table? = null
    var reader: Proc? = null

    @JvmField
    var insert: Proc? = null

    @JvmField
    var delete: Proc? = null

    @JvmField
    var update: Proc? = null

    @JvmField
    var title = ""

    @JvmField
    var cache: Proc? = null

    @JvmField
    var supplied: Vector<Field?>

    @JvmField
    var shows: Vector<Field?>

    @JvmField
    var cacheExtras: Vector<String>

    @JvmField
    var isViewOnly: Boolean

    @Throws(IOException::class)
    fun reader(ids: DataInputStream) {
        var isUsed = ids.readBoolean()
        reader = null
        if (isUsed == true) {
            val s = ids.readUTF()
            val p = table!!.getProc(s)
            if (p != null) reader = p
        }
        isUsed = ids.readBoolean()
        insert = null
        if (isUsed == true) {
            val s = ids.readUTF()
            val p = table!!.getProc(s)
            if (p != null) insert = p
        }
        isUsed = ids.readBoolean()
        delete = null
        if (isUsed == true) {
            val s = ids.readUTF()
            val p = table!!.getProc(s)
            if (p != null) delete = p
        }
        isUsed = ids.readBoolean()
        update = null
        if (isUsed == true) {
            val s = ids.readUTF()
            val p = table!!.getProc(s)
            if (p != null) update = p
        }
        title = ids.readUTF()
        isUsed = ids.readBoolean()
        cache = null
        if (isUsed == true) {
            val s = ids.readUTF()
            val p = table!!.getProc(s)
            if (p != null) cache = p
        }
        var noOf = ids.readInt()
        for (i in 0 until noOf) {
            val s = ids.readUTF()
            if (table!!.hasField(s)) supplied.addElement(table!!.getField(s))
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val s = ids.readUTF()
            if (table!!.hasField(s)) shows.addElement(table!!.getField(s))
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val s = ids.readUTF()
            cacheExtras.addElement(s)
        }
        isViewOnly = ids.readBoolean()
    }

    @Throws(IOException::class)
    fun writer(ods: DataOutputStream) {
        ods.writeBoolean(reader != null)
        if (reader != null) ods.writeUTF(reader!!.name)
        ods.writeBoolean(insert != null)
        if (insert != null) ods.writeUTF(insert!!.name)
        ods.writeBoolean(delete != null)
        if (delete != null) ods.writeUTF(delete!!.name)
        ods.writeBoolean(update != null)
        if (update != null) ods.writeUTF(update!!.name)
        ods.writeUTF(title)
        ods.writeBoolean(cache != null)
        if (cache != null) ods.writeUTF(cache!!.name)
        ods.writeInt(supplied.size)
        for (i in supplied.indices) {
            val f = supplied.elementAt(i)
            ods.writeUTF(f!!.name)
        }
        ods.writeInt(shows.size)
        for (i in shows.indices) {
            val f = shows.elementAt(i)
            ods.writeUTF(f!!.name)
        }
        ods.writeInt(cacheExtras.size)
        for (i in cacheExtras.indices) {
            val s = cacheExtras.elementAt(i)
            ods.writeUTF(s)
        }
        ods.writeBoolean(isViewOnly)
    }

    companion object {
        /**
         *
         */
        private const val serialVersionUID = 1L
    }

    init {
        supplied = Vector()
        shows = Vector()
        cacheExtras = Vector()
        isViewOnly = false
    }
}