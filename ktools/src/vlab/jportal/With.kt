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

class With : Serializable
{
    @JvmField
    var table: Table? = null
    @JvmField
    var name = ""
    @JvmField
    var lines: Vector<*>
    @JvmField
    var comments: Vector<*>
    @JvmField
    var options: Vector<*>
    @JvmField
    var start: Int
    @Throws(IOException::class)
    fun reader(ids: DataInputStream)
    {
        name = ids.readUTF()
        var noOf = ids.readInt()
        for (i in 0 until noOf)
        {
            val data = ids.readUTF()
            val isVar = ids.readBoolean()
            val value = Line(data, isVar)
            lines.addElement(value as Nothing?)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf)
        {
            val value = ids.readUTF()
            comments.addElement(value as Nothing?)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf)
        {
            val value = ids.readUTF()
            options.addElement(value as Nothing?)
        }
        start = ids.readInt()
    }

    @Throws(IOException::class)
    fun writer(ods: DataOutputStream)
    {
        ods.writeUTF(name)
        ods.writeInt(lines.size)
        for (i in lines.indices)
        {
            val value = lines.elementAt(i) as Line
            value.writer(ods)
        }
        ods.writeInt(comments.size)
        for (i in comments.indices)
        {
            val value = comments.elementAt(i) as String
            ods.writeUTF(value)
        }
        ods.writeInt(options.size)
        for (i in options.indices)
        {
            val value = options.elementAt(i) as String
            ods.writeUTF(value)
        }
        ods.writeInt(start)
    }

    /**
     * Folds the first character of name to an upper case character
     */
    fun upperFirst(): String
    {
        val f = name.substring(0, 1)
        return f.uppercase(Locale.getDefault()) + name.substring(1)
    }

    /**
     * Folds the first character of name to an upper case character
     */
    fun upperFirstOnly(): String
    {
        val f = name.substring(0, 1)
        return f.uppercase(Locale.getDefault())
    }

    /**
     * Folds the first character of name to an lower case character
     */
    fun lowerFirst(): String
    {
        val f = name.substring(0, 1)
        return f.lowercase(Locale.getDefault()) + name.substring(1)
    }

    companion object
    {
        private const val serialVersionUID = 1L
    }

    init
    {
        lines = Vector<Any?>()
        comments = Vector<Any?>()
        options = Vector<Any?>()
        start = 0
    }
}