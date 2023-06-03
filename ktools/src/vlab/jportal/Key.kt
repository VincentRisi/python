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
import java.util.*

/**
 * Keys and Indexes used for the database (if its not primary or unique then it is
 * an index)
 */
class Key : Serializable
{
    /**
     * Name of index or key
     */
    @JvmField
    var name = ""

    /**
     * List of fields used in the index or key
     */
    @JvmField
    var fields: Vector<String>
    @JvmField
    var options: Vector<String>

    /**
     * Indicates the primary key
     */
    @JvmField
    var isPrimary: Boolean

    /**
     * Indicates the index is unique (not defined if primary key)
     */
    @JvmField
    var isUnique: Boolean

    /**
     * Indicates the index is clustered (not defined if primary key)
     */
    @JvmField
    var isClustered: Boolean
    @Throws(IOException::class)
    fun reader(ids: DataInputStream)
    {
        name = ids.readUTF()
        var noOf = ids.readInt()
        for (i in 0 until noOf)
        {
            val value = ids.readUTF()
            fields.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf)
        {
            val value = ids.readUTF()
            options.addElement(value)
        }
        isPrimary = ids.readBoolean()
        isUnique = ids.readBoolean()
        isClustered = ids.readBoolean()
    }

    @Throws(IOException::class)
    fun writer(ods: DataOutputStream)
    {
        ods.writeUTF(name)
        ods.writeInt(fields.size)
        for (i in fields.indices)
        {
            val value = fields.elementAt(i)
            ods.writeUTF(value)
        }
        ods.writeInt(options.size)
        for (i in options.indices)
        {
            val value = options.elementAt(i)
            ods.writeUTF(value)
        }
        ods.writeBoolean(isPrimary)
        ods.writeBoolean(isUnique)
        ods.writeBoolean(isClustered)
    }

    /**
     * Checks if field is already used
     */
    fun hasField(s: String?): Boolean
    {
        var i: Int
        i = 0
        while (i < fields.size)
        {
            val name = fields.elementAt(i)
            if (name.equals(s, ignoreCase = true)) return true
            i++
        }
        return false
    }

    companion object
    {
        /**
         *
         */
        private const val serialVersionUID = 1L
    }

    /**
     * Contructs with default values
     */
    init
    {
        fields = Vector()
        options = Vector()
        isPrimary = false
        isUnique = false
        isClustered = false
    }
}