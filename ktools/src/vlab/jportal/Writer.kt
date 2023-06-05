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

import java.io.PrintWriter

object Writer {
    @JvmField
    var writer: PrintWriter? = null
    var indent_string = "                                                                                             "

    @JvmField
    var indent_size = 2
    var logger: PrintWriter? = null

    @JvmStatic
    fun format(fmt: String?, vararg objects: Any?): String {
        return String.format(fmt!!, *objects)
    }

    fun write(value: String?) {
        writer!!.print(value)
    }

    @JvmStatic
    fun write(no: Int, value: String) {
        writer!!.print(indent(no) + value)
    }

    fun writeln(no: Int, value: String) {
        writer!!.println(indent(no) + value)
    }

    fun writeln(value: String) {
        writeln(0, value)
    }

    @JvmStatic
    fun writeln() {
        writer!!.println()
    }

    fun indent(no: Int): String {
        val max = indent_string.length
        var to = no * indent_size
        if (to > max) to = max
        return indent_string.substring(0, to)
    }

    fun logln(line: String?) {
        logger!!.println(line)
    }
}