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

import java.io.FileInputStream
import java.io.ObjectInputStream
import java.io.PrintWriter
import java.io.Serializable
import java.util.*

/**
 * The Database identified by name, holds a list of tables for a
 * server, userid and password.
 */
class Database : Serializable
{
    @JvmField
    var name = ""
    @JvmField
    var output = ""
    @JvmField
    var server = ""
    @JvmField
    var schema = ""
    @JvmField
    var userid = ""
    @JvmField
    var password = ""
    @JvmField
    var packageName = ""
    @JvmField
    var portalName = ""
    @JvmField
    var tables: Vector<Table>
    @JvmField
    var flags: Vector<String>
    @JvmField
    var sequences: Vector<Sequence>
    @JvmField
    var views: Vector<View>
    @JvmField
    var imports: Vector<String>
    @JvmField
    var declares: Vector<Field>

    /**
     * Check for the existance of a table
     */
    fun hasTable(s: String?): Boolean
    {
        var i: Int
        i = 0
        while (i < tables.size)
        {
            val table = tables.elementAt(i)
            if (table.name.equals(s, ignoreCase = true)) return true
            i++
        }
        return false
    }

    /**
     * Return repository name root
     */
    fun outName(): String
    {
        return if (output.length > 0) output else name
    }

    private fun addinTable(tables: Vector<Table>, addin: Table, outLog: PrintWriter)
    {
        for (i in tables.indices)
        {
            var table = tables.elementAt(i)
            if (table.name.equals(addin.name, ignoreCase = true))
            {
                outLog.println("Import table name :${addin.name} to merge with existing.")
                table = table.add(addin, outLog)
                tables.setElementAt(table, i)
                return
            }
        }
        tables.addElement(addin)
    }

    private fun addinView(views: Vector<View>, addin: View, outLog: PrintWriter)
    {
        for (i in views.indices)
        {
            val view = views.elementAt(i)
            if (view.name.equals(addin.name, ignoreCase = true))
            {
                outLog.println("Import view name :${addin.name} already exists")
                return
            }
        }
        views.addElement(addin)
    }

    private operator fun set(a: String, b: String, what: String, outLog: PrintWriter): String
    {
        var a = a
        if (a.length == 0) a = b
        else if (a.equals(
                b,
                ignoreCase = true
            ) == false
        ) outLog.println("Import $what name :$a not the same as :$b")
        return a
    }

    fun add(database: Database, outLog: PrintWriter)
    {
        name = set(name, database.name, "name", outLog)
        output = set(output, database.output, "output", outLog)
        server = set(server, database.server, "server", outLog)
        userid = set(userid, database.userid, "userid", outLog)
        password = set(password, database.password, "password", outLog)
        packageName = set(packageName, database.packageName, "packageName", outLog)
        portalName = set(portalName, database.portalName, "portalName", outLog)
        for (i in database.tables.indices)
        {
            val table = database.tables.elementAt(i)
            addinTable(tables, table, outLog)
        }
        for (i in database.views.indices)
        {
            val view = database.views.elementAt(i)
            addinView(views, view, outLog)
        }
        for (i in database.sequences.indices)
        {
            val sequence = database.sequences.elementAt(i)
            addinSequence(sequences, sequence, outLog)
        }
        for (i in database.imports.indices)
        {
            var addinName = ""
            try
            {
                addinName = database.imports.elementAt(i)
                outLog.println("Addin name $addinName")
                var addIt = true
                for (j in imports.indices)
                {
                    val already = imports.elementAt(j)
                    if (already.equals(addinName, ignoreCase = true) == true)
                    {
                        addIt = false
                        outLog.println("Already imported: $addinName")
                        break
                    }
                }
                if (addIt == true)
                {
                    imports.addElement(addinName)
                    val next = readRepository(addinName, outLog)
                    add(next, outLog)
                }
            }
            catch (ex: Exception)
            {
                outLog.println("Import name :$addinName failed.")
            }
        }
    }

    fun doImports(outLog: PrintWriter): Database
    {
        if (imports.size > 0)
        {
            val database = Database()
            database.add(this, outLog)
            return database
        }
        return this
    }

    fun hasDeclare(fieldName: String): Boolean
    {
        for (i in declares.indices)
        {
            val field = declares.elementAt(i)
            if (fieldName.equals(field.name, ignoreCase = true) == true) return true
        }
        return false
    }

    fun getDeclare(fieldName: String): Field?
    {
        for (i in declares.indices)
        {
            val field = declares.elementAt(i)
            if (fieldName.equals(field.name, ignoreCase = true) == true) return field
        }
        return null
    }

    fun packageMerge(output: String): String
    {
        var output = output
        val ov = Vector<String>()
        val pv = Vector<String>()
        if (packageName.length == 0) return output
        val length = output.length
        var sep = output.lastIndexOf('/')
        var sepChar = '\\'
        if (sep != -1) sepChar = '/' else sep = output.lastIndexOf('\\')
        if (sep < length - 1) output = output + sepChar
        var work = "$packageName."
        var p = work.indexOf('.')
        while (p >= 0)
        {
            if (p > 0) pv.addElement(work.substring(0, p))
            work = work.substring(p + 1)
            p = work.indexOf('.')
        }
        work = output
        p = work.indexOf(sepChar)
        while (p >= 0)
        {
            if (p > 0) ov.addElement(work.substring(0, p))
            work = work.substring(p + 1)
            p = work.indexOf(sepChar)
        }
        var pw = pv.elementAt(0)
        var oi: Int
        var pi: Int
        oi = ov.size - 1
        while (oi >= 0)
        {
            val ow = ov.elementAt(oi)
            if (ow.compareTo(pw) == 0) break
            oi--
        }
        if (oi == -1) return output
        pi = 0
        while (oi < ov.size)
        {
            if (pi > pv.size - 1) break
            pw = pv.elementAt(pi)
            val ow = ov.elementAt(oi)
            if (ow.compareTo(pw) != 0) break
            pi++
            oi++
        }
        if (oi < ov.size) return output
        while (pi < pv.size)
        {
            pw = pv.elementAt(pi)
            output = output + pw + sepChar
            pi++
        }
        return output
    }

    companion object
    {
        /**
         *
         */
        private const val serialVersionUID = 1L
        @Throws(Exception::class)
        fun readRepository(name: String, outLog: PrintWriter): Database
        {
            outLog.println("Inputting $name.repository")
            val `in` = ObjectInputStream(FileInputStream("$name.repository"))
            return try
            {
                `in`.readObject() as Database
            }
            finally
            {
                `in`.close()
            }
        }

        private fun addinSequence(sequences: Vector<Sequence>, addin: Sequence, outLog: PrintWriter)
        {
            for (i in sequences.indices)
            {
                val sequence = sequences.elementAt(i)
                if (sequence.name.equals(addin.name, ignoreCase = true))
                {
                    outLog.println("Import sequence name :${addin.name} already exists")
                    return
                }
            }
            sequences.addElement(addin)
        }
    }

    init
    {
        tables = Vector()
        flags = Vector()
        sequences = Vector()
        views = Vector()
        imports = Vector()
        declares = Vector()
    }
}