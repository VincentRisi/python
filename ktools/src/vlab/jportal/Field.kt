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
 * This holds the field definition. It also supplies methods for the
 * Java format and various SQL formats.
 */
class Field : Serializable {
    /**
     * Name to use in the database
     */
    @JvmField
    var name = ""

    /**
     * Name to use in the database for a literal
     */
    @JvmField
    var literalName = ""

    /**
     * Name to use in the class if not present (normal case) then name is used
     */
    @JvmField
    var alias = ""

    /**
     * Default value to apply for the field on insert if not specified
     */
    @JvmField
    var defaultValue = ""

    /**
     * Check Constraint to applied to field by the database
     */
    @JvmField
    var checkValue = ""

    /**
     * Type of field
     */
    @JvmField
    var type: Byte = 0

    /**
     * Length of field
     */
    @JvmField
    var length = 0

    /**
     * No of digits in a numeric field
     */
    @JvmField
    var precision = 0

    /**
     * No of digits after the decimal point|comma
     */
    @JvmField
    var scale = 0
    var bindPos = 0
    var definePos = 0

    /**
     * Array of comments associated with the field
     */
    @JvmField
    var comments: Vector<String>

    @JvmField
    var enums: Vector<Enumerator>

    @JvmField
    var valueList: Vector<String>

    @JvmField
    var enumLink = ""

    /**
     * Indicates field is used in the primary key
     */
    var isPrimaryKey: Boolean

    /**
     * Indicates the field is a Sequence
     */
    @JvmField
    var isSequence: Boolean

    @JvmField
    var isIdentity: Boolean

    /**
     * Indicates the field can be NULL on the database
     */
    @JvmField
    var isNull: Boolean

    /**
     * Indicates the field can is a Literal
     */
    @JvmField
    var isLiteral: Boolean

    /**
     * Indicates the field is a calculated column on the database
     */
    @JvmField
    var isCalc: Boolean

    /**
     * Indicates the field is INPUT
     */
    @JvmField
    var isIn: Boolean

    /**
     * Indicates the field is OUTPUT
     */
    @JvmField
    var isOut: Boolean

    /**
     * Indicates the field is EXT
     */
    @JvmField
    var isExtStd: Boolean
    var isExtStdOut: Boolean

    @Throws(IOException::class)
    fun reader(ids: DataInputStream) {
        name = ids.readUTF()
        literalName = ids.readUTF()
        alias = ids.readUTF()
        checkValue = ids.readUTF()
        defaultValue = ids.readUTF()
        enumLink = ids.readUTF()
        type = ids.readByte()
        length = ids.readInt()
        precision = ids.readInt()
        scale = ids.readInt()
        bindPos = ids.readInt()
        definePos = ids.readInt()
        var noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readUTF()
            comments.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = Enumerator()
            value.reader(ids)
            enums.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = ids.readUTF()
            valueList.addElement(value)
        }
        isPrimaryKey = ids.readBoolean()
        isSequence = ids.readBoolean()
        isNull = ids.readBoolean()
        isLiteral = ids.readBoolean()
        isCalc = ids.readBoolean()
        isIn = ids.readBoolean()
        isExtStd = ids.readBoolean()
        isExtStdOut = ids.readBoolean()
        isOut = ids.readBoolean()
    }

    @Throws(IOException::class)
    fun writer(ods: DataOutputStream) {
        ods.writeUTF(name)
        ods.writeUTF(literalName)
        ods.writeUTF(alias)
        ods.writeUTF(checkValue)
        ods.writeUTF(defaultValue)
        ods.writeUTF(enumLink)
        ods.writeByte(type.toInt())
        ods.writeInt(length)
        ods.writeInt(precision)
        ods.writeInt(scale)
        ods.writeInt(bindPos)
        ods.writeInt(definePos)
        ods.writeInt(comments.size)
        for (i in comments.indices) {
            val value = comments.elementAt(i)
            ods.writeUTF(value)
        }
        ods.writeInt(enums.size)
        for (i in enums.indices) {
            val value = enums.elementAt(i)
            value.writer(ods)
        }
        ods.writeInt(valueList.size)
        for (i in valueList.indices) {
            val value = valueList.elementAt(i)
            ods.writeUTF(value)
        }
        ods.writeBoolean(isPrimaryKey)
        ods.writeBoolean(isSequence)
        ods.writeBoolean(isNull)
        ods.writeBoolean(isLiteral)
        ods.writeBoolean(isCalc)
        ods.writeBoolean(isIn)
        ods.writeBoolean(isExtStd)
        ods.writeBoolean(isExtStdOut)
        ods.writeBoolean(isOut)
    }

    /**
     * If there is an alias uses that else returns name
     */
    fun useName(): String {
        return if (alias.length > 0) alias else name
    }

    /**
     * If there is an alias uses that else returns name
     */
    fun useLowerName(): String {
        var n = useName()
        val f = n.substring(0, 1)
        if (isExtStd) {
            n = replaceAll(n, ".", "")
        }
        return f.lowercase(Locale.getDefault()) + n.substring(1)
    }

    /**
     * If there is an alias uses that else returns name
     */
    fun useUpperName(): String {
        var n = useName()
        val f = n.substring(0, 1)
        if (isExtStd) {
            n = replaceAll(n, ".", "")
        }
        return f.uppercase(Locale.getDefault()) + n.substring(1)
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

    /**
     * Check for empty string as null type fields.
     */
    val isEmptyAsNull: Boolean
        get() {
            if (isNull == false) return false
            when (type) {
                ANSICHAR -> {
                    if (length == 1) return false
                    return true
                }
                CHAR, DATE, DATETIME, TIME -> return true
            }
            return false
        }

    /**
     * Check for empty string as null type fields.
     */
    val isCharEmptyAsNull: Boolean
        get() {
            if (isNull == false) return false
            when (type) {
                ANSICHAR -> {
                    if (length == 1) return false
                    return true
                }
                CHAR, TLOB -> return true
            }
            return false
        }

    /**
     * Check for empty string as null type fields.
     */
    fun ansiIsNull(): Boolean {
        return if (isNull == false) false else type == ANSICHAR && length == 1
    }

    val isEmptyOrAnsiAsNull: Boolean
        get() = isEmptyAsNull || ansiIsNull()
    val isCharEmptyOrAnsiAsNull: Boolean
        get() = isCharEmptyAsNull || ansiIsNull()

    /**
     * If there is an literal uses that else returns name
     * optional inString defaults to false
     * returning escaped quotes or double quotes
     */
    @JvmOverloads
    fun useLiteral(inString: Boolean = false): String {
        if (isLiteral) {
            if (inString) {
                val first = literalName[0]
                val no = literalName.length - 1
                val last = literalName[no]
                if (no > 0 && first == last) if (first == '"' || first == '\'') return "\\" + literalName.substring(
                    0,
                    no
                ) + "\\" + last
            }
            return literalName
        }
        return name
    }

    fun fixEscape(): String {
        var result = useLiteral(false)
        if (result[0] == '[') result = result.replace('[', '"').replace(']', '"')
        else if (result[0] == '`') result = result.replace('`', '"')
        return result
    }

    val isEnum: Boolean
        get() = enums.size > 0

    companion object {
        const val BLOB: Byte = 1
        const val BOOLEAN: Byte = 2
        const val BYTE: Byte = 3
        const val CHAR: Byte = 4
        const val DATE: Byte = 5
        const val DATETIME: Byte = 6
        const val DOUBLE: Byte = 7
        const val DYNAMIC: Byte = 8
        const val FLOAT: Byte = 9
        const val IDENTITY: Byte = 10
        const val INT: Byte = 11
        const val LONG: Byte = 12
        const val MONEY: Byte = 13
        const val SEQUENCE: Byte = 14
        const val SHORT: Byte = 15
        const val STATUS: Byte = 16
        const val TIME: Byte = 17
        const val TIMESTAMP: Byte = 18
        const val TLOB: Byte = 19
        const val USERSTAMP: Byte = 20
        const val ANSICHAR: Byte = 21
        const val UID: Byte = 22
        const val XML: Byte = 23
        const val BIGSEQUENCE: Byte = 24
        const val BIGIDENTITY: Byte = 25
        const val AUTOTIMESTAMP: Byte = 26
        const val WCHAR: Byte = 27
        const val WANSICHAR: Byte = 28
        const val UTF8: Byte = 29
        const val BIGXML: Byte = 30
        const val IMAGE: Byte = 31
        const val UNICODE: Byte = 32
        const val DEFAULT_XML = 4096
        const val DEFAULT_BIG_XML = 4194304

        /**
         *
         */
        private const val serialVersionUID = 1L
    }

    /**
     * constructor ensures fields have correct default values
     */
    init {
        comments = Vector()
        enums = Vector()
        valueList = Vector()
        isPrimaryKey = false
        isSequence = false
        isIdentity = false
        isNull = false
        isLiteral = false
        isCalc = false
        isIn = false
        isExtStd = false
        isExtStdOut = false
        isOut = false
    }
}