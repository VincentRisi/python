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
 * Views of table
 */
class View : Serializable
{
    /**
     * Name of view
     */
    @JvmField
    var name = ""

    /**
     * List of aliases from view
     */
    @JvmField
    var aliases: Vector<*>

    /**
     * SQL Code for view
     */
    @JvmField
    var lines: Vector<*>

    /**
     * Users of the view
     */
    @JvmField
    var users: Vector<*>

    /**
     * Code starts at line
     */
    @JvmField
    var start: Int
    @Throws(IOException::class)
    fun reader(ids: DataInputStream)
    {
        name = ids.readUTF()
        var noOf = ids.readInt()
        for (i in 0 until noOf)
        {
            val value = ids.readUTF()
            aliases.addElement(value as Nothing?)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf)
        {
            val value = ids.readUTF()
            lines.addElement(value as Nothing?)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf)
        {
            val value = ids.readUTF()
            users.addElement(value as Nothing?)
        }
        start = ids.readInt()
    }

    @Throws(IOException::class)
    fun writer(ods: DataOutputStream)
    {
        ods.writeUTF(name)
        ods.writeInt(aliases.size)
        for (i in aliases.indices)
        {
            val value = aliases.elementAt(i) as String
            ods.writeUTF(value)
        }
        ods.writeInt(lines.size)
        for (i in lines.indices)
        {
            val value = lines.elementAt(i) as String
            ods.writeUTF(value)
        }
        ods.writeInt(users.size)
        for (i in users.indices)
        {
            val value = users.elementAt(i) as String
            ods.writeUTF(value)
        }
        ods.writeInt(start)
    }

    /**
     * Checks if view has alias
     */
    fun hasAlias(s: String?): Boolean
    {
        var i: Int
        i = 0
        while (i < aliases.size)
        {
            val alias = aliases.elementAt(i) as String
            if (alias.equals(s, ignoreCase = true)) return true
            i++
        }
        return false
    }

    /**
     * Checks if view has user
     */
    fun hasUser(s: String?): Boolean
    {
        var i: Int
        i = 0
        while (i < users.size)
        {
            val name = users.elementAt(i) as String
            if (name.equals(s, ignoreCase = true)) return true
            i++
        }
        return false
    }

    override fun toString(): String
    {
        return name
    }

    companion object
    {
        /**
         *
         */
        private const val serialVersionUID = 1L
    }

    /**
     * Constructs the view with proper defaults
     */
    init
    {
        aliases = Vector<Any?>()
        lines = Vector<Any?>()
        users = Vector<Any?>()
        start = 0
    }
}