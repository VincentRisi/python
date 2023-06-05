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
 * This is used to hold the grants and users of Table and Procedures
 */
class Grant : Serializable {
    /**
     * List of Permissions
     */
    @JvmField
    var perms: Vector<String>

    /**
     * List of Users for the List of Permissions
     */
    @JvmField
    var users: Vector<String>

    @Throws(IOException::class)
    fun reader(ids: DataInputStream) {
        var noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readUTF()
            perms.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readUTF()
            users.addElement(value)
        }
    }

    @Throws(IOException::class)
    fun writer(ods: DataOutputStream) {
        ods.writeInt(perms.size)
        for (i in perms.indices) {
            val value = perms.elementAt(i)
            ods.writeUTF(value)
        }
        ods.writeInt(users.size)
        for (i in users.indices) {
            val value = users.elementAt(i)
            ods.writeUTF(value)
        }
    }

    /**
     * Check if permission is used
     */
    fun hasPerm(s: String?): Boolean {
        for (i in perms.indices) {
            val name = perms.elementAt(i)
            if (name.equals(s, ignoreCase = true)) return true
        }
        return false
    }

    /**
     * Check if user has been defined
     */
    fun hasUser(s: String?): Boolean {
        for (i in users.indices) {
            val name = users.elementAt(i)
            if (name.equals(s, ignoreCase = true)) return true
        }
        return false
    }

    companion object {
        /**
         *
         */
        private const val serialVersionUID = 1L
    }

    /**
     * Construct default values
     */
    init {
        perms = Vector()
        users = Vector()
    }
}