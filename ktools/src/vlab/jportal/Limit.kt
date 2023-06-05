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

import java.io.Serializable
import java.util.ArrayList

class Limit : Serializable {
    @JvmField
    var count = 0

    @JvmField
    var variable: String? = null

    @JvmField
    var size = 0
    fun fetchRowsSize(): Int {
        var result = 0
        if (variable == null) result += String.format("\"\\nFETCH FIRST %d ROWS ONLY\"", count).length
        else {
            result += "\"\\nFETCH FIRST \"".length
            result += size
            result += "\"\\nROWS ONLY\\n\"".length
        }
        return result
    }

    fun fetchRowsLines(): Array<String> {
        val code: ArrayList<String>
        code = ArrayList()
        return if (variable == null) {
            code.add(String.format("    strcat(q_.command, \"\\nFETCH FIRST %d ROWS ONLY\");", count))
            code.toTypedArray()
        } else {
            code.add("    strcat(q_.command, \"\\nFETCH FIRST \");")
            code.add(String.format("    strcat(q_.command, %s);", variable))
            code.add("    strcat(q_.command, \" ROWS ONLY\\n\");")
            code.toTypedArray()
        }
    }

    fun fetchRowsLinesDBApi(): Array<String> {
        val code: ArrayList<String>
        code = ArrayList()
        return if (variable == null) {
            code.add(String.format("FETCH FIRST %d ROWS ONLY", count))
            code.toTypedArray()
        } else {
            code.add("FETCH FIRST ")
            code.add(String.format("{self.%s}", variable))
            code.add(" ROWS ONLY")
            code.toTypedArray()
        }
    }

    fun topRowsSize(): Int {
        var result = 0
        if (variable == null) result += String.format("\"TOP %d \");", count).length
        else {
            result += "\"TOP \");".length
            result += size
        }
        return result
    }

    fun topRowsLines(): Array<String> {
        val code: ArrayList<String>
        code = ArrayList()
        return if (variable == null) {
            code.add(String.format("    strcat(q_.command, \"TOP %d \");", count))
            code.toTypedArray()
        } else {
            code.add("    strcat(q_.command, \"TOP \");")
            code.add(String.format("    strcat(q_.command, %s);", variable))
            code.add("    strcat(q_.command, \"\\n\");")
            code.toTypedArray()
        }
    }

    fun topRowsLinesDBApi(): Array<String> {
        val code: ArrayList<String>
        code = ArrayList()
        return if (variable == null) {
            code.add(String.format("TOP %d ", count))
            code.toTypedArray()
        } else {
            code.add("TOP ")
            code.add(String.format("{self.%s}", variable))
            code.toTypedArray()
        }
    }

    fun limitRowsSize(): Int {
        var result = 0
        if (variable == null) result += String.format("\"\\nLIMIT %d\"", count).length
        else {
            result += "\"\\nLIMIT \"".length
            result += size
        }
        return result
    }

    fun limitRowsLines(): Array<String> {
        val code: ArrayList<String>
        code = ArrayList()
        return if (variable == null) {
            code.add(String.format("    strcat(q_.command, \"\\nLIMIT %d \");", count))
            code.toTypedArray()
        } else {
            code.add("    strcat(q_.command, \"\\nLIMIT \");")
            code.add(String.format("    strcat(q_.command, %s);", variable))
            code.add("    strcat(q_.command, \"\\n\");")
            code.toTypedArray()
        }
    }

    fun limitRowsLinesDBApi(): Array<String> {
        val code: ArrayList<String>
        code = ArrayList()
        return if (variable == null) {
            code.add(String.format("LIMIT %d ", count))
            code.toTypedArray()
        } else {
            code.add("LIMIT ")
            code.add(String.format("{self.%s} ", variable))
            code.toTypedArray()
        }
    }

    companion object {
        /**
         *
         */
        private const val serialVersionUID = 1L
    }
}