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
import java.lang.StringBuffer
import java.util.*

/**
 * Foreign keys used in database
 */
class Link : Serializable {
    /**
     * Name of foreign table
     */
    @JvmField
    var name = ""
    var linkName = ""

    @JvmField
    var fields: Vector<String>

    @JvmField
    var linkFields: Vector<String>

    @JvmField
    var options: Vector<*>

    @JvmField
    var isDeleteCascade: Boolean

    @JvmField
    var isUpdateCascade: Boolean
    var isProc: Boolean
    var isDProc: Boolean

    @Throws(IOException::class)
    fun reader(ids: DataInputStream) {
        name = ids.readUTF()
        linkName = ids.readUTF()
        var noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readUTF()
            fields.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readUTF()
            linkFields.addElement(value)
        }
        isDeleteCascade = ids.readBoolean()
    }

    @Throws(IOException::class)
    fun writer(ods: DataOutputStream) {
        ods.writeUTF(name)
        ods.writeUTF(linkName)
        ods.writeInt(fields.size)
        for (i in fields.indices) {
            val value = fields.elementAt(i)
            ods.writeUTF(value)
        }
        for (i in linkFields.indices) {
            val value = linkFields.elementAt(i)
            ods.writeUTF(value)
        }
        ods.writeBoolean(isDeleteCascade)
    }

    fun hasField(s: String?): Boolean {
        var i: Int
        i = 0
        while (i < fields.size) {
            val name = fields.elementAt(i)
            if (name.equals(s, ignoreCase = true)) return true
            i++
        }
        return false
    }

    /**
     * If there is an alias uses that else returns name
     */
    fun useName(): String {
        var n = name
        n = replaceAll(n, ".", "_")
        return n
    }

    fun replaceAll(
        haystack: String,  // String to search in
        needle: String,  // Substring to find
        replacement: String?
    ): String {         // Substring to replace with
        var haystack = haystack
        var i = haystack.lastIndexOf(needle)
        if (i != -1) {
            val buffer = StringBuffer(haystack)
            buffer.replace(i, i + needle.length, replacement)
            while (haystack.lastIndexOf(needle, i - 1).also { i = it } != -1) {
                buffer.replace(i, i + needle.length, replacement)
            }
            haystack = buffer.toString()
        }
        return haystack
    }

    companion object {
        /**
         *
         */
        private const val serialVersionUID = 1L
    }

    init {
        fields = Vector()
        linkFields = Vector()
        options = Vector<Any?>()
        isDeleteCascade = false
        isUpdateCascade = false
        isProc = false
        isDProc = false
    }
}