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

/**
 * The hearts and souls. Holds the procedures for accessing the table.
 */
class Proc : Serializable {
    /**
     * parent table
     */
    @JvmField
    var table: Table? = null

    /**
     * name of procedure
     */
    @JvmField
    var name = ""

    /**
     * name of rows on multiples
     */
    @JvmField
    var noRows = 0

    /**
     * List of input fields
     */
    @JvmField
    var inputs: Vector<Field>

    /**
     * List of output fields
     */
    @JvmField
    var outputs: Vector<Field>

    /**
     * List of dynamic SQL code fields
     */
    @JvmField
    var dynamics: Vector<String>

    /**
     * List of dynamic SQL code field sizes
     */
    @JvmField
    var dynamicSizes: Vector<Int>

    /**
     * List of dynamic SQL code field sizes
     */
    @JvmField
    var dynamicStrung: Vector<Boolean>

    /**
     * SQL code for accessing the table
     */
    var placeHolders: Vector<String>

    /**
     * SQL code for accessing the table
     */
    var lines: Vector<Line>

    /**
     * The reasons and debates for the procedure
     */
    @JvmField
    var comments: Vector<String>

    /**
     * Generate options for procedure
     */
    @JvmField
    var options: Vector<String>

    /**
     * SelectBy DeleteBy std proc fields
     */
    @JvmField
    var fields: Vector<String>

    /**
     * SelectFor update fields
     */
    @JvmField
    var updateFields: Vector<String>

    /**
     * Select in order fields
     */
    @JvmField
    var orderFields: Vector<String>

    /**
     * Select in order fields
     */
    @JvmField
    var withs: Vector<String>

    /**
     * Indicates the procedure uses stored procedure logic Code
     */
    @JvmField
    var isProc: Boolean

    /**
     * Indicates the procedure uses stored procedure logic Code
     */
    @JvmField
    var isSProc: Boolean

    /**
     * If the procedure is only to produce passthru SQL Code
     */
    @JvmField
    var isData: Boolean

    /**
     * If the procedure is only to produce passthru SQL Code
     */
    @JvmField
    var isIdlCode: Boolean

    /**
     * Indicates the procedure is internal SQL code
     */
    @JvmField
    var isSql: Boolean

    /**
     * Indicates a single result is expected
     */
    @JvmField
    var isSingle: Boolean

    /**
     * Indicates a update Proc
     */
    @JvmField
    var isUpdate: Boolean

    /**
     * Indicates an action no result is expected
     */
    var isAction: Boolean

    /**
     * Indicates procedure is a Standard procedure
     */
    @JvmField
    var isStd: Boolean

    /**
     * Indicates the procedure uses the Standard Table definition
     */
    @JvmField
    var useStd: Boolean

    /**
     * Indicates the procedures extends the Standard Table definition
     */
    @JvmField
    var extendsStd: Boolean

    /**
     * Indicates the procedures uses the Primary key
     */
    var useKey: Boolean

    /**
     * Indicates the procedure has an Image field
     */
    var hasImage: Boolean

    /**
     * Indicates a single result is expected
     */
    @JvmField
    var isMultipleInput: Boolean

    /**
     * Indicates the procedure is the Insert procedure
     */
    @JvmField
    var isInsert: Boolean

    /**
     *
     */
    var isMerge: Boolean

    /**
     *
     */
    @JvmField
    var hasReturning: Boolean

    /**
     *
     */
    @JvmField
    var hasUpdates: Boolean

    /**
     * Code starts at line
     */
    @JvmField
    var start: Int

    @JvmField
    var useUpsert: Boolean
    fun copy(from: Proc) {
        name = from.name
        noRows = from.noRows
        inputs = from.inputs
        outputs = from.outputs
        dynamics = from.dynamics
        dynamicSizes = from.dynamicSizes
        dynamicStrung = from.dynamicStrung
        placeHolders = from.placeHolders
        lines = from.lines
        comments = from.comments
        options = from.options
        fields = from.fields
        updateFields = from.updateFields
        orderFields = from.orderFields
        withs = from.withs
        isProc = from.isProc
        isSProc = from.isSProc
        isData = from.isData
        isIdlCode = from.isIdlCode
        isSql = from.isSql
        isAction = from.isAction
        isSingle = from.isSingle
        isUpdate = from.isUpdate
        isStd = from.isStd
        useStd = from.useStd
        extendsStd = from.extendsStd
        useKey = from.useKey
        hasImage = from.hasImage
        isInsert = from.isInsert
        isMerge = from.isMerge
        isMultipleInput = from.isMultipleInput
        hasReturning = from.hasReturning
        hasUpdates = from.hasUpdates
        start = from.start
        useUpsert = from.useUpsert
    }

    fun addLine(line: Line) {
        lines.addElement(line)
    }

    fun addLine(data: String?, isVar: Boolean) {
        val value = Line(data!!, isVar)
        addLine(value)
    }

    fun addLine(line: String?) {
        addLine(line, false)
    }

    @Throws(IOException::class)
    fun reader(ids: DataInputStream) {
        name = ids.readUTF()
        noRows = ids.readInt()
        var noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = Field()
            value.reader(ids)
            inputs.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = Field()
            value.reader(ids)
            outputs.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readUTF()
            dynamics.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readInt()
            dynamicSizes.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readBoolean()
            dynamicStrung.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readUTF()
            placeHolders.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val data = ids.readUTF()
            val isVar = ids.readBoolean()
            val value = Line(data, isVar)
            addLine(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readUTF()
            comments.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readUTF()
            options.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readUTF()
            fields.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readUTF()
            updateFields.addElement(value)
        }
        isProc = ids.readBoolean()
        isSProc = ids.readBoolean()
        isData = ids.readBoolean()
        isIdlCode = ids.readBoolean()
        isSql = ids.readBoolean()
        isAction = ids.readBoolean()
        isSingle = ids.readBoolean()
        isUpdate = ids.readBoolean()
        isStd = ids.readBoolean()
        useStd = ids.readBoolean()
        extendsStd = ids.readBoolean()
        useKey = ids.readBoolean()
        hasImage = ids.readBoolean()
        isInsert = ids.readBoolean()
        isMultipleInput = ids.readBoolean()
        hasReturning = ids.readBoolean()
        hasUpdates = ids.readBoolean()
        start = ids.readInt()
    }

    @Throws(IOException::class)
    fun writer(ods: DataOutputStream) {
        ods.writeUTF(name)
        ods.writeInt(noRows)
        ods.writeInt(inputs.size)
        for (i in inputs.indices) {
            val value = inputs.elementAt(i)
            value.writer(ods)
        }
        ods.writeInt(outputs.size)
        for (i in outputs.indices) {
            val value = outputs.elementAt(i)
            value.writer(ods)
        }
        ods.writeInt(dynamics.size)
        for (i in dynamics.indices) {
            val value = dynamics.elementAt(i)
            ods.writeUTF(value)
        }
        ods.writeInt(dynamicSizes.size)
        for (i in dynamicSizes.indices) {
            val value = dynamicSizes.elementAt(i)
            ods.writeInt(value.toInt())
        }
        ods.writeInt(dynamicStrung.size)
        for (i in dynamicStrung.indices) {
            val value = dynamicStrung.elementAt(i)
            ods.writeBoolean(value)//.toBoolean())
        }
        ods.writeInt(placeHolders.size)
        for (i in placeHolders.indices) {
            val value = placeHolders.elementAt(i)
            ods.writeUTF(value)
        }
        ods.writeInt(lines.size)
        for (i in lines.indices) {
            val value = lines.elementAt(i)
            value.writer(ods)
        }
        ods.writeInt(comments.size)
        for (i in comments.indices) {
            val value = comments.elementAt(i)
            ods.writeUTF(value)
        }
        ods.writeInt(options.size)
        for (i in options.indices) {
            val value = options.elementAt(i)
            ods.writeUTF(value)
        }
        ods.writeInt(fields.size)
        for (i in fields.indices) {
            val value = fields.elementAt(i)
            ods.writeUTF(value)
        }
        ods.writeInt(updateFields.size)
        for (i in updateFields.indices) {
            val value = updateFields.elementAt(i)
            ods.writeUTF(value)
        }
        ods.writeBoolean(isProc)
        ods.writeBoolean(isSProc)
        ods.writeBoolean(isData)
        ods.writeBoolean(isIdlCode)
        ods.writeBoolean(isSql)
        ods.writeBoolean(isAction)
        ods.writeBoolean(isSingle)
        ods.writeBoolean(isUpdate)
        ods.writeBoolean(isStd)
        ods.writeBoolean(useStd)
        ods.writeBoolean(extendsStd)
        ods.writeBoolean(useKey)
        ods.writeBoolean(hasImage)
        ods.writeBoolean(isInsert)
        ods.writeBoolean(isMultipleInput)
        ods.writeBoolean(hasReturning)
        ods.writeBoolean(hasUpdates)
        ods.writeInt(start)
    }

    /**
     * Folds the first character of name to an upper case character
     */
    fun upperFirst(): String {
        if (name.length < 1) {
            println("Table:$table name length appears to be less than 1")
            return name
        }
        val f = name.substring(0, 1)
        return f.uppercase(Locale.getDefault()) + name.substring(1)
    }

    /**
     * Folds the first character of name to an upper case character
     */
    fun upperFirstOnly(): String {
        if (name.length < 1) {
            println("Table:$table name length appears to be less than 1")
            return name
        }
        val f = name.substring(0, 1)
        return f.uppercase(Locale.getDefault())
    }

    /**
     * Folds the first character of name to an lower case character
     */
    fun lowerFirst(): String {
        if (name.length < 1) {
            println("Table:$table name length appears to be less than 1")
            return name
        }
        val f = name.substring(0, 1)
        return f.lowercase(Locale.getDefault()) + name.substring(1)
    }

    /**
     * Checks for for name in input list
     */
    fun hasInput(s: String?): Boolean {
        for (i in inputs.indices) {
            val field = inputs.elementAt(i)
            if (field.name.equals(s, ignoreCase = true)) return true
        }
        return false
    }

    fun getInput(s: String?): Field? {
        for (i in inputs.indices) {
            val field = inputs.elementAt(i)
            if (field.name.equals(s, ignoreCase = true)) return field
        }
        return null
    }

    fun hasModifieds(): Boolean {
        for (i in inputs.indices) {
            val field = inputs.elementAt(i)
            if (field.type == Field.SEQUENCE && isInsert == true
                || field.type == Field.BIGSEQUENCE && isInsert == true
                || field.type == Field.USERSTAMP || field.type == Field.TIMESTAMP
            ) return true
        }
        return false
    }

    /**
     * Checks for for name in input list
     */
    fun indexOf(s: String?): Int {
        for (i in inputs.indices) {
            val field = inputs.elementAt(i)
            if (field.name.equals(s, ignoreCase = true)) return i
        }
        return -1
    }

    /**
     * Checks for for name in output list
     */
    fun hasOutput(s: String?): Boolean {
        for (i in outputs.indices) {
            val field = outputs.elementAt(i)
            if (field.name.equals(s, ignoreCase = true)) return true
        }
        return false
    }

    /**
     * Checks for for name in output list
     */
    fun getOutput(s: String?): Field? {
        for (i in outputs.indices) {
            val field = outputs.elementAt(i)
            if (field.name.equals(s, ignoreCase = true)) return field
        }
        return null
    }

    /**
     * Checks for for name in dynamics list
     */
    fun hasDynamic(s: String): Boolean {
        for (i in dynamics.indices) {
            val name = dynamics.elementAt(i)
            if (name == s) return true
        }
        return false
    }

    /**
     * Checks for for name in dynamics list
     */
    fun getDynamicSize(s: String): Int {
        for (i in dynamics.indices) {
            val name = dynamics.elementAt(i)
            if (name == s) {
                val n = dynamicSizes.elementAt(i)
                return n.toInt()
            }
        }
        return 256
    }

    /**
     * Checks if a strung dynamic
     */
    fun isStrung(s: String): Boolean {
        for (i in dynamics.indices) {
            val name = dynamics.elementAt(i)
            if (name == s) {
                val b = dynamicStrung.elementAt(i)
                return b //.toBoolean()
            }
        }
        return false
    }

    /**
     * Checks if proc uses data
     */
    fun hasNoData(): Boolean {
        return inputs.size == 0 && outputs.size == 0 && dynamics.size == 0
    }

    /**
     * Checks if proc has unique input ie. not already in output
     */
    fun hasDiscreteInput(): Boolean {
        if (dynamics.size > 0) return true
        for (i in inputs.indices) {
            val field = inputs.elementAt(i)
            if (hasOutput(field.name)) continue
            return true
        }
        return false
    }

    /**
     *
     */
    fun checkPlaceHolders() {
        for (i in lines.indices) {
            val code = lines.elementAt(i)
            if (code.isVar == true) continue
            var work = code.line.uppercase(Locale.getDefault())
            var work2 = code.line
            val alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_#$"
            val alphanum = alpha + "0123456789"
            var n = work.indexOf(':')
            while (n != -1) {
                work = work.substring(n + 1)
                work2 = work2.substring(n + 1)
                var p = 0
                if (alpha.indexOf(work[0]) != -1) {
                    p = 1
                    while (p < work.length) {
                        if (alphanum.indexOf(work[p]) == -1) break
                        p++
                    }
                }
                if (p > 1) {
                    val placeHolder = work2.substring(0, p)
                    if (hasInput(placeHolder)) placeHolders.addElement(placeHolder) else println("placeHolder($placeHolder) is not defined as an Input for proc($name)")
                }
                n = work.indexOf(':')
            }
        }
    }

    override fun toString(): String {
        return name
    }

    fun hasOption(value: String): Boolean {
        for (i in options.indices) {
            val option = options.elementAt(i)
            if (option.lowercase(Locale.getDefault()).compareTo(value.lowercase(Locale.getDefault())) == 0) return true
        }
        return false
    }

    fun hasFields(value: String): Boolean {
        for (i in fields.indices) {
            val option = fields.elementAt(i)
            if (option.lowercase(Locale.getDefault()).compareTo(value.lowercase(Locale.getDefault())) == 0) return true
        }
        return false
    }

    fun hasOrders(value: String): Boolean {
        for (i in orderFields.indices) {
            val option = orderFields.elementAt(i)
            if (option.lowercase(Locale.getDefault()).compareTo(value.lowercase(Locale.getDefault())) == 0) return true
        }
        return false
    }

    fun hasUpdateFields(value: String): Boolean {
        for (i in updateFields.indices) {
            val option = updateFields.elementAt(i)
            if (option.lowercase(Locale.getDefault()).compareTo(value.lowercase(Locale.getDefault())) == 0) return true
        }
        return false
    }

    val isStdExtended: Boolean
        get() {
            if (isStd == true) return true
            if (extendsStd == true) {
                if (useStd == true) return true
                if (dynamics.size > 0) return false
                for (i in inputs.indices) {
                    val field = inputs.elementAt(i)
                    if (table!!.hasField(field.name) == false) return false
                }
                for (i in outputs.indices) {
                    val field = outputs.elementAt(i)
                    if (table!!.hasField(field.name) == false) return false
                }
                return true
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
     * Constructs with default values
     */
    init {
        inputs = Vector()
        outputs = Vector()
        dynamics = Vector()
        dynamicSizes = Vector()
        dynamicStrung = Vector()
        placeHolders = Vector()
        lines = Vector()
        comments = Vector()
        options = Vector()
        fields = Vector()
        updateFields = Vector()
        orderFields = Vector()
        withs = Vector()
        isProc = false
        isSProc = false
        isData = false
        isIdlCode = false
        isSql = false
        isAction = false
        isSingle = false
        isUpdate = false
        isStd = false
        useStd = false
        extendsStd = false
        useKey = false
        hasImage = false
        isInsert = false
        isMerge = false
        isMultipleInput = false
        hasReturning = false
        hasUpdates = false
        start = 0
        useUpsert = false
    }
}