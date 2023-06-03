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

import java.io.*
import java.lang.ClassNotFoundException
import java.lang.SecurityException
import java.lang.NoSuchMethodException
import java.lang.IllegalArgumentException
import java.lang.IllegalAccessException
import java.lang.reflect.InvocationTargetException
import java.lang.NullPointerException

object Compiler
{
    private var outLog: PrintWriter? = null
    private var inputs: String? = null
    private var nubDir: String? = null
    private var rootDir = ""
    @Throws(
        FileNotFoundException::class,
        ClassNotFoundException::class,
        SecurityException::class,
        NoSuchMethodException::class,
        IllegalArgumentException::class,
        IllegalAccessException::class,
        InvocationTargetException::class
    )
    fun compile(source: String, args: Array<String>, outLog: PrintWriter?): Int
    {
        var outLog = outLog
        val pieces = source.split("\\+".toRegex()).toTypedArray()
        var database: Database? = null
        var hasErrors = false
        for (p in pieces.indices)
        {
            val db: Database = JPortal.run(pieces[p], nubDir, outLog)
            when {
                database != null -> {
                    for (t in db.tables.indices) database.tables.addElement(db.tables.elementAt(t))
                    for (s in db.sequences.indices) database.sequences.addElement(db.sequences.elementAt(s))
                    for (v in db.views.indices) database.views.addElement(db.views.elementAt(v))
                }
                else -> {
                    database = db
                }
            }
        }
        if (hasErrors == true) return 1
        outLog!!.flush()
        var output = ""
        var reported = false
        var i = 0
        while (i < args.size)
        {
            if (args[i] == "-o")
            {
                if (i + 1 < args.size)
                {
                    output = checkRoot(args[++i])
                    var term = '\\'
                    if (output.indexOf('/') != -1) term = '/'
                    val ch = output[output.length - 1]
                    if (ch != term) output = output + term
                }
                i++
                continue
            }
            else if (args[i] == "-R")
            {
                if (i + 1 < args.size) rootDir = args[++i] else rootDir = ""
                i++
                continue
            }
            else if (args[i] == "-l")
            {
                if (i + 1 < args.size)
                {
                    val log = args[++i]
                    val outFile: OutputStream = FileOutputStream(log)
                    outLog!!.flush()
                    outLog = PrintWriter(outFile)
                }
                i++
                continue
            }
            else if (args[i] == "-f" || args[i] == "-F")
            {
                if (i + 1 < args.size)
                {
                    val flag = args[++i]
                    database!!.flags.addElement(flag)
                }
                i++
                continue
            }
            else if (args[i][0] == '-')
            {
                if (reported == false)
                {
                    reported = true
                    if (args[i].length > 1)
                    {
                        val sw = args[i][1]
                        outLog!!.println(String.format("Valid compile switch arguments here are (%c)", sw))
                        outLog.println(" -o <name>     Directory to place output")
                        outLog.println(" -(F|f) <flag> Flag to add to Database flags")
                        outLog.println(" -l <name>     Change logging name")
                    }
                }
                i++
                continue
            }
            outLog!!.println(args[i])
            val c = Class.forName("vlab.jportal." + args[i])
            val d = arrayOf(database!!.javaClass, output.javaClass, outLog.javaClass)
            val m = c.getMethod("generate", *d)
            val o = arrayOf<Any?>(database, output, outLog)
            m.invoke(database, *o)
            i++
        }
        outLog!!.flush()
        return 0
    }

    private fun checkRoot(name: String): String
    {
        if (rootDir.length == 0) return name
        if (name.startsWith("{root}")) return rootDir + name.substring(6)
        return if (name.startsWith("\${root}")) rootDir + name.substring(7) else name
    }

    @Throws(IOException::class)
    private fun frontSwitches(args: Array<String>): Array<String>
    {
        var log = ""
        var i = 0
        var reported = false
        while (true)
        {
            if (args.size > i && args[i] == "-l")
            {
                if (i + 1 < args.size)
                {
                    log = args[++i]
                    val outFile: OutputStream = FileOutputStream(log)
                    outLog!!.flush()
                    outLog = PrintWriter(outFile)
                }
                i++
                continue
            }
            if (args[i] == "-R")
            {
                if (i + 1 < args.size) rootDir = args[++i] else rootDir = ""
                i++
                continue
            }
            if (args.size > i && args[i] == "-n")
            {
                if (i + 1 < args.size) nubDir = args[++i]
                i++
                continue
            }
            if (args.size > i && (args[i] == "-f" || args[i] == "-i"))
            {
                if (i + 1 < args.size)
                {
                    val fileName = checkRoot(args[++i])
                    val fileReader = FileReader(fileName)
                    val bufferedReader = BufferedReader(fileReader)
                    try
                    {
                        var semicolon = if (inputs!!.length > 0) ";" else ""
                        while (bufferedReader.ready())
                        {
                            val line = checkRoot(bufferedReader.readLine())
                            inputs = inputs + semicolon + line
                            semicolon = ";"
                        }
                    }
                    catch (e2: NullPointerException)
                    {
                    }
                }
                i++
                break
            }
            if (args.size > i && args[i][0] == '-')
            {
                if (reported == false)
                {
                    reported = true
                    if (args[i].length > 1)
                    {
                        val sw = args[i][1]
                        outLog!!.println(String.format("Valid front switch arguments here are (%c)", sw))
                        outLog!!.println(" -l <name>     Change logging name")
                        outLog!!.println(" -(i|f) <name> File for list of .si files to compile")
                        outLog!!.println(" -n <name>     Not really used nubdir")
                    }
                }
                i++
                continue
            }
            break
        }
        if (args.size > i && inputs!!.length == 0)
        {
            inputs = args[i]
            i++
        }
        val newargs: Array<String> = Array<String>((args.size - i), { "" })
        System.arraycopy(args, i, newargs, 0, newargs.size)
        return newargs
    }

    private fun abbreviate(inputs: String?): String?
    {
        val sources = inputs!!.split(";".toRegex()).toTypedArray()
        return if (sources.size > 5) sources[0] + " ... " + sources[sources.size - 1] else inputs
    }

    /**
     * Reads input from stored repository
     */
    @JvmStatic
    fun main(args: Array<String>)
    {
        var args = args
        try
        {
            outLog = PrintWriter(System.out)
            inputs = ""
            nubDir = ""
            args = frontSwitches(args)
            println(abbreviate(inputs))
            if (args.size < 2)
            {
                outLog!!.println("usage java jportal.Compiler -l log (-(i|f) inputs | infile) (generators)+")
                outLog!!.println("for example to create DDL for Sql Server and Java, VB and Delphi code")
                outLog!!.println()
                outLog!!.println("java jportal.Compiler airline.si (-(F|f) flag)* -o ./dir1 MSSqlDDL -o ./dir2 JavaCode -o ./dir3 VBCode -o ./dir4 DelphiCode")
                outLog!!.flush()
                System.exit(1)
            }
            outLog!!.println(inputs)
            outLog!!.flush()
            val sources = inputs!!.split(";".toRegex()).toTypedArray()
            for (f in sources.indices)
            {
                val rc = compile(sources[f], args, outLog)
                outLog!!.flush()
                if (rc != 0) System.exit(1)
            }
            System.exit(0)
        }
        catch (e: Throwable)
        {
            e.printStackTrace()
            outLog!!.println("Error: $e")
            outLog!!.flush()
            System.exit(1)
        }
    }
}