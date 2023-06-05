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
import java.util.*

/**
 * Table identified by name holds fields, keys, links, grants, views and
 * procedures associated with the table.
 */
class Table : Serializable {
    @JvmField
    var database: Database? = null

    @JvmField
    var literalName = ""

    @JvmField
    var name = ""

    @JvmField
    var alias = ""

    @JvmField
    var check = ""

    @JvmField
    var fields: Vector<Field?>

    @JvmField
    var keys: Vector<Key?>

    @JvmField
    var links: Vector<Link?>

    @JvmField
    var grants: Vector<Grant?>

    @JvmField
    var views: Vector<View?>

    @JvmField
    var procs: Vector<Proc?>

    @JvmField
    var withs: Vector<With?>

    @JvmField
    var comments: Vector<String?>

    @JvmField
    var options: Vector<String?>
    var allUsers: Vector<*>

    @JvmField
    var parameters: Vector<*>

    @JvmField
    var consts: Vector<*>

    @JvmField
    var hasPrimaryKey: Boolean

    @JvmField
    var hasSequence: Boolean

    @JvmField
    var hasTimeStamp: Boolean

    @JvmField
    var hasAutoTimeStamp: Boolean

    @JvmField
    var hasUserStamp: Boolean

    @JvmField
    var hasExecute: Boolean

    @JvmField
    var hasSelect: Boolean

    @JvmField
    var hasInsert: Boolean

    @JvmField
    var hasDelete: Boolean

    @JvmField
    var hasUpdate: Boolean

    @JvmField
    var hasStdProcs: Boolean

    @JvmField
    var hasIdentity: Boolean

    @JvmField
    var hasSequenceReturning: Boolean

    @JvmField
    var hasBigXML: Boolean
    var isStoredProc: Boolean

    @JvmField
    var isLiteral: Boolean

    @JvmField
    var start: Int

    @JvmOverloads
    @Throws(IOException::class)
    fun reader(ids: DataInputStream, useProcs: Vector<*>? = null) {
        val signature = ids.readInt()
        if (signature != 0xBABA00D) return
        name = ids.readUTF()
        literalName = ids.readUTF()
        alias = ids.readUTF()
        check = ids.readUTF()
        var noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = Field()
            value.reader(ids)
            fields.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = Key()
            value.reader(ids)
            keys.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = Link()
            value.reader(ids)
            links.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = Grant()
            value.reader(ids)
            grants.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = View()
            value.reader(ids)
            views.addElement(value)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = Proc()
            value.reader(ids)
            if (useProcs == null) procs.addElement(value)
            else for (p in useProcs.indices) {
                val name = useProcs.elementAt(p) as String
                if (value.name.compareTo(name, true) === 0) {
                    procs.addElement(value)
                    break
                }
            }
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = With()
            value.reader(ids)
            withs.addElement(value)
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
            val value = Parameter()
            value.table = this
            value.reader(ids)
            parameters.addElement(value as Nothing?)
        }
        noOf = ids.readInt()
        for (i in 0 until noOf) {
            val value = Const()
            value.reader(ids)
            consts.addElement(value as Nothing?)
        }
        hasExecute = ids.readBoolean()
        hasSelect = ids.readBoolean()
        hasInsert = ids.readBoolean()
        hasDelete = ids.readBoolean()
        hasUpdate = ids.readBoolean()
        hasPrimaryKey = ids.readBoolean()
        hasSequence = ids.readBoolean()
        hasTimeStamp = ids.readBoolean()
        hasAutoTimeStamp = ids.readBoolean()
        hasUserStamp = ids.readBoolean()
        hasStdProcs = ids.readBoolean()
        hasIdentity = ids.readBoolean()
        hasSequenceReturning = ids.readBoolean()
        isStoredProc = ids.readBoolean()
        isLiteral = ids.readBoolean()
        start = ids.readInt()
    }

    @Throws(IOException::class)
    fun writer(ods: DataOutputStream) {
        ods.writeInt(0xBABA00D)
        ods.writeUTF(name)
        ods.writeUTF(literalName)
        ods.writeUTF(alias)
        ods.writeUTF(check)
        ods.writeInt(fields.size)
        for (i in fields.indices) {
            val value = fields.elementAt(i)
            value!!.writer(ods)
        }
        ods.writeInt(keys.size)
        for (i in keys.indices) {
            val value = keys.elementAt(i)
            value!!.writer(ods)
        }
        ods.writeInt(links.size)
        for (i in links.indices) {
            val value = links.elementAt(i)
            value!!.writer(ods)
        }
        ods.writeInt(grants.size)
        for (i in grants.indices) {
            val value = grants.elementAt(i)
            value!!.writer(ods)
        }
        ods.writeInt(views.size)
        for (i in views.indices) {
            val value = views.elementAt(i)
            value!!.writer(ods)
        }
        var noProcs = 0
        for (i in procs.indices) {
            val value: Proc? = procs.elementAt(i)
            if (value != null && value.isData)
                continue
            noProcs++
        }
        ods.writeInt(noProcs)
        for (i in procs.indices) {
            val value: Proc? = procs.elementAt(i)
            if (value != null) {
                if (value.isData == true) continue
                value.writer(ods)
            }
        }
        ods.writeInt(withs.size)
        for (i in withs.indices) {
            val value: With? = withs.elementAt(i)
            if (value != null) value.writer(ods)
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
        ods.writeInt(parameters.size)
        for (i in parameters.indices) {
            val value: Parameter = parameters.elementAt(i) as Parameter
            value.table = this
            value.writer(ods)
        }
        ods.writeInt(consts.size)
        for (i in consts.indices) {
            val value = consts.elementAt(i) as Const
            value.writer(ods)
        }
        ods.writeBoolean(hasExecute)
        ods.writeBoolean(hasSelect)
        ods.writeBoolean(hasInsert)
        ods.writeBoolean(hasDelete)
        ods.writeBoolean(hasUpdate)
        ods.writeBoolean(hasPrimaryKey)
        ods.writeBoolean(hasSequence)
        ods.writeBoolean(hasTimeStamp)
        ods.writeBoolean(hasAutoTimeStamp)
        ods.writeBoolean(hasUserStamp)
        ods.writeBoolean(hasStdProcs)
        ods.writeBoolean(hasIdentity)
        ods.writeBoolean(hasSequenceReturning)
        ods.writeBoolean(isStoredProc)
        ods.writeBoolean(isLiteral)
        ods.writeInt(start)
    }

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

    fun useExtra(extra: String): String {
        val name = fixEscape()
        var work = name + extra
        val last = name.length - 1
        if (name[0] == '\"' && name[last] == '\"') work = name.substring(0, last - 1) + extra + name.substring(last)
        return work
    }

    /**
     * If there is an alias uses that else returns name
     */
    fun useName(): String {
        return if (alias.length > 0) alias else name
    }

    /**
     * Checks for the existence of a with
     */
    fun hasWith(s: String?): Boolean {
        for (i in withs.indices) {
            val with: With? = withs.elementAt(i)
            if (with != null && with.name.equals(s, true)) return true
        }
        return false
    }

    fun getWith(s: String?): With? {
        for (i in withs.indices) {
            val with: With? = withs.elementAt(i)
            if (with != null && with.name.equals(s, true)) return with
        }
        return null
    }

    /**
     * Checks for the existence of a field
     */
    fun hasField(s: String?): Boolean {
        var i: Int
        i = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.name.equals(s, ignoreCase = true)) return true
            i++
        }
        return false
    }

    fun getField(s: String?): Field? {
        var i: Int
        i = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.name.equals(s, ignoreCase = true)) return field
            i++
        }
        return null
    }

    fun getFieldIndex(s: String?): Int {
        var i: Int
        i = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.name.equals(s, ignoreCase = true)) return i
            i++
        }
        return -1
    }

    /**
     * Checks if table field is declared as null
     */
    fun hasFieldAsNull(s: String?): Boolean {
        var i: Int
        i = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.name.equals(s, ignoreCase = true)) return field.isNull
            i++
        }
        return false
    }

    /**
     * Checks for the existence of a proc
     */
    fun hasProc(p: Proc): Boolean {
        for (i in procs.indices) {
            val proc: Proc? = procs.elementAt(i)
            if (proc != null && proc.name.equals(p.name, true)) return true
        }
        return false
    }

    /**
     * Returns proc or null
     */
    fun getProc(name: String?): Proc? {
        for (i in procs.indices) {
            val proc: Proc? = procs.elementAt(i)
            if (proc != null && proc.name.equals(name, true)) return proc
        }
        return null
    }

    /**
     * Checks for the existence of a proc
     */
    fun hasCursorStdProc(): Boolean {
        for (i in procs.indices) {
            val proc: Proc? = procs.elementAt(i)
            if (proc == null) return false
            if (proc.isStd === true && proc.isSingle === false && proc.outputs.size > 0) return true
        }
        return false
    }

    /**
     * Sets a field to be primary key
     */
    fun setPrimary(s: String?) {
        var i: Int
        i = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.name.equals(s, ignoreCase = true)) {
                field.isPrimaryKey = true
                return
            }
            i++
        }
    }

    fun tableName(): String {
        return if (database!!.schema.length == 0) useLiteral(true) else database!!.schema + "." + useLiteral(true)
    }

    /**
     * Builds a merge proc generated as part of standard record class
     */
    fun buildMerge(proc: Proc) {
        val name = tableName()
        var i: Int
        var comma = "   "
        var front = ""
        //proc.isStd = true;
        //proc.extendsStd = true;
        proc.isSql = true
        proc.isMerge = true
        proc.lines.addElement(Line("merge into $name"))
        proc.lines.addElement(Line(" using (select"))
        i = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            proc.inputs.addElement(field)
            proc.lines.addElement(Line(comma + ":" + field!!.name + " as " + field.name))
            comma = " , "
            i++
        }
        val dualType = Line("DUAL_TYPE")
        dualType.isVar = true
        val dualSize = 256
        proc.lines.addElement(dualType)
        proc.dynamics.addElement("DUAL_TYPE")
        proc.dynamicSizes.addElement(dualSize)
        proc.dynamicStrung.addElement(false)
        proc.lines.addElement(Line(") as temp_" + proc.table!!.name))
        front = " on ("
        i = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.isPrimaryKey) {
                proc.lines.addElement(
                    Line(
                        front + name + "." + field.useLiteral(true)
                                + " = temp_" + proc.table!!.name + "." + field.useLiteral(true)
                    )
                )
                front = " and "
            }
            i++
        }
        proc.lines.addElement(Line(")"))
        proc.lines.addElement(Line(" when matched"))
        proc.lines.addElement(Line("  then update set"))
        comma = "    "
        i = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.isPrimaryKey == false) {
                proc.lines.addElement(
                    Line(
                        comma + name + "." + field.useLiteral(true)
                                + " = temp_" + proc.table!!.name + "." + field.useLiteral(true)
                    )
                )
                comma = "  , "
            }
            i++
        }
        //    comma = "  where ";
//    for (i = 0; i < fields.size(); i++)
//    {
//      Field field = fields.elementAt(i);
//      if (field.isPrimaryKey == false)
//      {
//        proc.lines.addElement(new Line(comma + name + "." + field.useLiteral(true)
//                + " <> temp_" + proc.table.name + "." + field.useLiteral(true)));
//        comma = "     or ";
//      }
//    }
        proc.lines.addElement(Line(" when not matched"))
        proc.lines.addElement(Line("  then insert"))
        proc.lines.addElement(Line("  ("))
        comma = "    "
        i = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            proc.lines.addElement(Line(comma + field!!.useLiteral(true)))
            comma = "  , "
            i++
        }
        proc.lines.addElement(Line("  )"))
        proc.lines.addElement(Line("  values"))
        proc.lines.addElement(Line("  ("))
        comma = "    "
        i = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)

            proc.lines.addElement(
                Line(
                    front + name + "." + field!!.useLiteral(true)
                            + " = temp_" + proc.table!!.name + "." + field.useLiteral(true)
                )
            )
            comma = "  , "
            i++
        }
        proc.lines.addElement(Line("  );"))
    }

    /**
     * Builds an insert proc generated as part of standard record class
     */
    fun buildInsert(proc: Proc) {
        val name = tableName()
        var i: Int
        var line = "  "
        proc.isStd = true
        proc.isSql = true
        proc.isInsert = true
        if (proc.hasReturning) {
            var allow_ret = false
            for (field in fields) {
                if (field!!.isSequence || field.isIdentity) {
                    allow_ret = true
                    break
                }
            }
            proc.hasReturning = allow_ret
        }
        if (proc.hasReturning && proc.table!!.hasIdentity == false) proc.lines.add(Line("_ret.head", true))
        var identityName = ""
        proc.lines.addElement(Line("insert into $name ("))
        i = 0
        while (i < fields.size) {
            val comma = if (i + 1 < fields.size) "," else ""
            val field = fields.elementAt(i)
            if (field!!.isCalc) {
                i++
                continue
            }
            if (isIdentity(field) == true) {
                hasIdentity = true
                identityName = field.name
                proc.outputs.addElement(field)
                proc.isSingle = true
                proc.hasUpdates = true
                i++
                continue
            }
            if (isSequence(field) == true && proc.hasReturning === true) {
                proc.outputs.addElement(field)
                proc.isSingle = true
                proc.hasUpdates = true
                proc.lines.addElement(Line("_ret.checkUse(\"" + line + field.useLiteral(true) + comma + "\")", true))
                i++
                continue
            } else if (isSequence(field) == true && proc.isMultipleInput === true) {
                proc.lines.addElement(Line("_ret.checkUse(\"" + line + field.useLiteral(true) + comma + "\")", true))
                i++
                continue
            } else if (isSequence(field) == true && proc.hasReturning === false) {
                proc.inputs.addElement(field)
                proc.lines.addElement(Line(line + field.useLiteral(true) + comma))
                proc.hasUpdates = true
                i++
                continue
            }
            proc.inputs.addElement(field)
            proc.lines.addElement(Line(line + field.useLiteral(true) + comma))
            i++
        }
        proc.lines.addElement(Line(" ) "))
        if (hasIdentity == true) proc.lines.addElement(Line(" output inserted.$identityName"))
        else if (proc.hasReturning) proc.lines.addElement(
            Line("_ret.output", true)
        )
        proc.lines.addElement(Line(" values ("))
        i = 0
        while (i < fields.size) {
            val comma = if (i + 1 < fields.size) "," else ""
            val field = fields.elementAt(i)
            if (isIdentity(field) == true || field!!.isCalc) {
                i++
                continue
            }
            if (isSequence(field) == true && proc.hasReturning === true) proc.lines.addElement(
                Line(
                    "_ret.sequence",
                    true
                )
            )
            else if (isSequence(field) == true && proc.isMultipleInput === true) proc.lines.addElement(
                Line("_ret.sequence", true)
            )
            else if (isSequence(field) == true && proc.hasReturning === false) {
                proc.lines.addElement(Line(line + " :" + field.useLiteral(true) + comma))
                i++
                continue
            } else proc.lines.addElement(Line(line + " :" + field.useLiteral(true) + comma))
            line = "  "
            i++
        }
        proc.lines.addElement(Line(" )"))
        if (proc.hasReturning && proc.table!!.hasIdentity == false) proc.lines.add(Line("_ret.tail", true))
        if (proc.useUpsert) proc.lines.addElement(Line(" /*use upsert*/"))
    }

    /**
     * Builds an insert proc generated as part of standard record class
     */
    fun buildBulkInsert(proc: Proc) {
        proc.isMultipleInput = true
        buildInsert(proc)
    }

    /**
     * Builds an identity proc generated as part of standard record class
     */
    fun buildIdentity(proc: Proc) {
        val name = tableName()
        var i: Int
        var line: String
        proc.isSql = true
        proc.isSingle = true
        i = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.type != Field.IDENTITY) {
                i++
                continue
            }
            proc.outputs.addElement(field)
            line = "select max(" + field.useLiteral(true) + ") " + field.useLiteral(true) + " from " + name
            proc.lines.addElement(Line(line))
            i++
        }
    }

    /**
     * Builds an update proc generated as part of standard record class
     */
    fun buildUpdate(proc: Proc) {
        val name = tableName()
        var i: Int
        var j: Int
        var line: String
        proc.isStd = true
        proc.isSql = true
        proc.lines.addElement(Line("update $name"))
        proc.lines.addElement(Line(" set"))
        i = 0
        j = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.isPrimaryKey || field.isCalc || field.isSequence) {
                i++
                continue
            }
            proc.inputs.addElement(field)
            line = if (j == 0) "  " else ", "
            j++
            proc.lines.addElement(Line(line + field.useLiteral(true) + " = :" + field.useLiteral(true)))
            i++
        }
        i = 0
        j = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.isPrimaryKey) {
                proc.inputs.addElement(field)
                line = if (j == 0) " where " else "   and "
                j++
                line = line + field.useLiteral(true) + " = :" + field.useLiteral(true)
                proc.lines.addElement(Line(line))
            }
            i++
        }
        if (proc.hasReturning) proc.lines.add(Line("_ret.tail", true))
    }

    /**
     * Builds an update proc generated as part of standard record class
     */
    open fun buildUpdateFor(proc: Proc, outLog: PrintWriter?) {
        val name = tableName()
        var i: Int
        var j: Int
        var k: Int
        var line: String
        proc.isStd = true
        proc.isSql = true
        proc.lines.addElement(Line("update $name"))
        proc.lines.addElement(Line(" set"))
        i = 0
        j = 0
        while (i < proc.fields.size) {
            val fieldName = proc.fields.elementAt(i)
            k = 0
            while (k < fields.size) {
                val field = fields.elementAt(k)!!
                if (field.isPrimaryKey || field.isCalc || field.isSequence) {
                    k++
                    continue
                }
                if (field.name.equals(fieldName, ignoreCase = true)) {
                    proc.inputs.addElement(field)
                    line = if (j == 0) "  " else ", "
                    j++
                    proc.lines.addElement(Line(line + field.useLiteral(true) + " = :" + field.useLiteral(true)))
                }
                k++
            }
            i++
        }
        AddTimeStampUserStamp(proc)
        i = 0
        j = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)!!
            if (field.isPrimaryKey) {
                proc.inputs.addElement(field)
                line = if (j == 0) " where " else "   and "
                j++
                line = line + field.useLiteral(true) + " = :" + field.useLiteral(true)
                proc.lines.addElement(Line(line))
            }
            i++
        }
        if (proc.hasReturning) proc.lines.add(Line("_ret.tail", true))
    }

    /**
     * Builds an updateby proc generated as part of standard record class
     */
    open fun buildUpdateBy(proc: Proc, outLog: PrintWriter?) {
        val name = tableName()
        var i: Int
        var j: Int
        var k: Int
        var line: String
        proc.isStd = true
        proc.isSql = true
        proc.lines.addElement(Line("update $name"))
        proc.lines.addElement(Line(" set"))
        if (proc.fields.size == 0) {
            k = 0
            while (k < proc.updateFields.size) {
                val fieldName = proc.updateFields.elementAt(k)
                i = 0
                j = 0
                while (i < fields.size) {
                    val field = fields.elementAt(i)!!
                    if (field.isPrimaryKey || field.isCalc || field.name.equals(
                            fieldName,
                            ignoreCase = true
                        ) || field.isSequence
                    ) {
                        i++
                        continue
                    }
                    proc.inputs.addElement(field)
                    line = if (j == 0) "  " else ", "
                    j++
                    proc.lines.addElement(Line(line + field.useLiteral(true) + " = :" + field.useLiteral(true)))
                    i++
                }
                k++
            }
        } else {
            i = 0
            j = 0
            while (i < proc.fields.size) {
                val fieldName = proc.fields.elementAt(i)
                k = 0
                while (k < fields.size) {
                    val field = fields.elementAt(k)!!
                    if (field.name.equals(fieldName, ignoreCase = true)) {
                        proc.inputs.addElement(field)
                        line = if (j == 0) "  " else ", "
                        j++
                        proc.lines.addElement(Line(line + field.useLiteral(true) + " = :" + field.useLiteral(true)))
                    }
                    k++
                }
                i++
            }
        }
        AddTimeStampUserStamp(proc)
        i = 0
        j = 0
        while (i < proc.updateFields.size) {
            val fieldName = proc.updateFields.elementAt(i)
            k = 0
            while (k < fields.size) {
                val field = fields.elementAt(k)!!
                if (field.name.equals(fieldName, ignoreCase = true)) {
                    proc.inputs.addElement(field)
                    line = if (j == 0) " where " else "   and "
                    j++
                    line = line + field.useLiteral(true) + " = :" + field.useLiteral(true)
                    proc.lines.addElement(Line(line))
                }
                k++
            }
            i++
        }
        if (proc.hasReturning) proc.lines.add(Line("_ret.tail", true))
    }

    private fun AddTimeStampUserStamp(proc: Proc) {
        var k: Int
        var line: String
        var tmAdded: Boolean
        var unAdded: Boolean
        unAdded = false
        tmAdded = unAdded
        k = 0
        while (k < fields.size) {
            val field = fields.elementAt(k)
            if (field!!.type == Field.USERSTAMP && !unAdded) {
                unAdded = true
                if (!proc.inputs.contains(field)) {
                    proc.inputs.addElement(field)
                    line = ", "
                    proc.lines.addElement(Line(line + field.useLiteral(true) + " = " + field.useLiteral(true)))
                }
            } else if (field.type == Field.TIMESTAMP && !tmAdded) {
                tmAdded = true
                if (!proc.inputs.contains(field)) {
                    proc.inputs.addElement(field)
                    line = ", "
                    proc.lines.addElement(Line(line + field.useLiteral(true) + " = " + field.useLiteral(true)))
                }
            }
            k++
        }
    }

    /**
     * Builds an update proc generated as part of standard record class
     */
    fun buildBulkUpdate(proc: Proc) {
        proc.isMultipleInput = true
        buildUpdate(proc)
    }

    /**
     * Builds a delete by primary key proc
     */
    fun buildDeleteOne(proc: Proc) {
        val name = tableName()
        var i: Int
        var j: Int
        var line: String
        proc.isSql = true
        proc.lines.addElement(Line("delete from $name"))
        i = 0
        j = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.isPrimaryKey) {
                proc.inputs.addElement(field)
                line = if (j == 0) " where " else "   and "
                j++
                line = line + field.useLiteral(true) + " = :" + field.useLiteral(true)
                proc.lines.addElement(Line(line))
            }
            i++
        }
        if (proc.hasReturning) proc.lines.add(Line("_ret.tail", true))
    }

    /**
     * Builds a delete all rows proc
     */
    fun buildDeleteAll(proc: Proc) {
        val name = tableName()
        proc.isSql = true
        proc.lines.addElement(Line("delete from $name"))
        if (proc.hasReturning) proc.lines.add(Line("_ret.tail", true))
    }

    /**
     * Builds a count rows proc
     */
    fun buildCount(proc: Proc) {
        val name = tableName()
        proc.isSql = true
        proc.isSingle = true
        val noOf = Field()
        noOf.name = "noOf"
        noOf.type = Field.INT
        noOf.length = 4
        proc.outputs.addElement(noOf)
        proc.lines.addElement(Line("select count(*) noOf from $name"))
    }

    /**
     * Builds a check for primary key existance proc
     */
    fun buildExists(proc: Proc) {
        val name = tableName()
        var i: Int
        var j: Int
        var line: String
        proc.isSql = true
        proc.isSingle = true
        val noOf = Field()
        noOf.name = "noOf"
        noOf.type = Field.INT
        noOf.length = 4
        proc.outputs.addElement(noOf)
        proc.lines.addElement(Line("select count(*) noOf from $name"))
        i = 0
        j = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.isPrimaryKey) {
                proc.inputs.addElement(field)
                line = if (j == 0) " where " else "   and "
                j++
                line = line + field.useLiteral(true) + " = :" + field.useLiteral(true)
                proc.lines.addElement(Line(line))
            }
            i++
        }
    }

    /**
     * Builds a select on primary key proc
     */
    fun buildSelectOne(proc: Proc, update: Boolean, readonly: Boolean) {
        val name = tableName()
        var i: Int
        var j: Int
        var line: String
        proc.isStd = true
        proc.isSql = true
        proc.isSingle = true
        proc.lines.addElement(Line("select"))
        i = 0
        j = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (!field!!.isPrimaryKey) {
                proc.outputs.addElement(field)
                line = if (j == 0) "  " else ", "
                j++
                proc.lines.addElement(Line(line + field.useLiteral(true)))
            }
            i++
        }
        proc.lines.addElement(Line(" from $name"))
        i = 0
        j = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.isPrimaryKey) {
                proc.inputs.addElement(field)
                line = if (j == 0) " where " else "   and "
                j++
                line = line + field.useLiteral(true) + " = :" + field.useLiteral(true)
                proc.lines.addElement(Line(line))
            }
            i++
        }
        if (update) proc.lines.addElement(Line(" for update")) else if (readonly) proc.lines.addElement(Line(" for read only"))
    }

    /**
     * Builds a select on primary key proc
     */
    fun buildMaxTmStamp(proc: Proc) {
        val name = tableName()
        var i: Int
        proc.isStd = true
        proc.isSql = true
        proc.isSingle = true
        proc.lines.addElement(Line("select "))
        i = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            if (field!!.type == Field.TIMESTAMP) {
                proc.outputs.addElement(field)
                proc.lines.addElement(Line("max(" + field.useLiteral(true) + ")"))
            }
            i++
        }
        proc.lines.addElement(Line(" from $name"))
    }

    /**
     * Builds a select all rows proc
     */
    fun buildSelectAll(proc: Proc, update: Boolean, readonly: Boolean, inOrder: Boolean, descending: Boolean) {
        val name = tableName()
        var i: Int
        var n: Int
        var line: String
        proc.isStd = true
        proc.isSql = true
        proc.lines.addElement(Line("select"))
        i = 0
        while (i < fields.size) {
            val field = fields.elementAt(i)
            proc.outputs.addElement(field)
            line = if (i == 0) "  " else ", "
            proc.lines.addElement(Line(line + field!!.useLiteral(true)))
            i++
        }
        proc.lines.addElement(Line(" from $name"))
        selectFor(proc, update, readonly)
        selectOrderBy(proc, inOrder, descending)
    }

//    private fun selectOrderBy(proc: Proc, inOrder: Boolean, descending: Boolean)
//    {
//        var i: Int
//        val n: Int
//        var line: String
//        var tail: String
//        if (inOrder == false) return
//        if (proc.orderFields.size() === 0)
//        {
//            i = 0
//            while (i < fields.size)
//            {
//                val field = fields.elementAt(i)
//                if (field!!.isPrimaryKey) proc.orderFields.addElement(field.useLiteral(true))
//                i++
//            }
//        }
//        n = proc.orderFields.size()
//        i = 0
//        while (i < n)
//        {
//            val fieldName: String = proc.orderFields.elementAt(i)
//            line = if (i == 0) " order by " else ", "
//            tail = if (descending == true && i + 1 == n) " desc" else ""
//            proc.lines.addElement(Line(line + fieldName + tail))
//            i++
//        }
//    }

    private fun selectOrderBy(proc: Proc, inOrder: Boolean, descending: Boolean) {
        var i: Int
        val n: Int
        var line: String
        var tail: String
        if (inOrder == false) return
        if (proc.orderFields.size == 0) {
            i = 0
            while (i < fields.size) {
                val field = fields.elementAt(i)!!
                if (field.isPrimaryKey) proc.orderFields.addElement(field.useLiteral(true))
                i++
            }
        }
        n = proc.orderFields.size
        i = 0
        while (i < n) {
            val fieldName = proc.orderFields.elementAt(i)
            line = if (i == 0) " order by " else ", "
            tail = if (descending == true && i + 1 == n) " desc" else ""
            proc.lines.addElement(Line(line + fieldName + tail))
            i++
        }
    }

    private fun selectFor(proc: Proc, update: Boolean, readonly: Boolean) {
        if (update) proc.lines.addElement(Line(" for update")) else if (readonly) proc.lines.addElement(Line(" for read only"))
    }

    fun buildDeleteBy(proc: Proc, outLog: PrintWriter?) {
        val name = tableName()
        var i: Int
        var j: Int
        var k: Int
        var line: String
        proc.isStd = true
        proc.isSql = true
        proc.lines.addElement(Line("Delete from $name"))
        i = 0
        j = 0
        while (i < proc.fields.size) {
            val fieldName = proc.fields.elementAt(i)
            k = 0
            while (k < fields.size) {
                val field = fields.elementAt(k)!!
                if (field.name.equals(fieldName, ignoreCase = true)) {
                    proc.inputs.addElement(field)
                    line = if (j == 0) " where " else "   and "
                    j++
                    line = line + field.useLiteral(true) + " = :" + field.useLiteral(true)
                    proc.lines.addElement(Line(line))
                }
                k++
            }
            i++
        }
        if (proc.hasReturning) proc.lines.add(Line("_ret.tail", true))
        if (j == 0) {
            throw java.lang.Error("Error generating buildDeleteBy")
        }
    }

    fun buildSelectBy(
        proc: Proc, forUpdate: Boolean, forReadOnly: Boolean, inOrder: Boolean, descending: Boolean,
        outLog: PrintWriter?
    ) {
        val name = tableName()
        var i: Int
        var j: Int
        var k: Int
        var line: String
        proc.isStd = true
        proc.isSql = true
        proc.lines.addElement(Line("select"))
        if (proc.outputs.size > 0) {
            i = 0
            while (i < proc.outputs.size) {
                val fieldOut = proc.outputs.elementAt(i)
                k = 0
                while (k < fields.size) {
                    val field = fields.elementAt(k)!!
                    if (field.name.equals(fieldOut.name, ignoreCase = true)) {
                        line = if (i == 0) "  " else ", "
                        proc.lines.addElement(Line(line + field.useLiteral(true)))
                    }
                    k++
                }
                i++
            }
        } else {
            i = 0
            while (i < fields.size) {
                val field = fields.elementAt(i)!!
                proc.outputs.addElement(field)
                line = if (i == 0) "  " else ", "
                proc.lines.addElement(Line(line + field.useLiteral(true)))
                i++
            }
        }
        proc.lines.addElement(Line(" from $name"))
        selectFor(proc, forUpdate, forReadOnly)
        i = 0
        j = 0
        while (i < proc.fields.size) {
            val fieldName = proc.fields.elementAt(i)
            k = 0
            while (k < fields.size) {
                val field = fields.elementAt(k)!!
                if (field.name.equals(fieldName, ignoreCase = true)) {
                    proc.inputs.addElement(field)
                    line = if (j == 0) " where " else "   and "
                    j++
                    line = line + field.useLiteral(true) + " = :" + field.useLiteral(true)
                    proc.lines.addElement(Line(line))
                }
                k++
            }
            i++
        }
        if (j == 0) {
            throw Error("Error in SelectBy")
        }
        selectOrderBy(proc, inOrder, descending)
    }

    fun buildSelectFrom(proc: Proc, table: Table, outLog: PrintWriter) {
        val name = tableName()
        var i: Int
        var j: Int
        var k: Int
        var line: String
        proc.extendsStd = false
        proc.isSql = true
        var preFix = ""
        var doSelect = true
        var first: Line
        if (proc.lines.size > 0) {
            first = proc.lines.elementAt(0)
            k = 0
            while (k < proc.lines.size) {
                first = proc.lines.elementAt(k)
                if (first.line.lowercase(Locale.getDefault())
                        .indexOf("select ") > -1 && first.line.lowercase(Locale.getDefault()).indexOf("select ") < 5
                ) {
                    doSelect = false
                    outLog.println(
                        "Select found not generating SELECT." + first.line.lowercase(Locale.getDefault())
                            .indexOf("select ")
                    )
                    break
                }
                k++
            }
        }
        if (doSelect) {
            if (preFix === "") {
                k = 0
                while (k < proc.lines.size) {
                    first = proc.lines.elementAt(k)
                    if (first.line.lowercase(Locale.getDefault()).indexOf(name.lowercase(Locale.getDefault())) > -1) {
                        preFix = first.line.substring(
                            first.line.lowercase(Locale.getDefault())
                                .indexOf(name.lowercase(Locale.getDefault())) + name.length
                        ).trim { it <= ' ' }
                        val n = preFix.indexOf(' ')
                        if (n > 0) {
                            preFix = preFix.substring(0, n).trim { it <= ' ' }
                        }
                        if (!name.lowercase(Locale.getDefault())
                                .startsWith(preFix.lowercase(Locale.getDefault()).substring(0, 1))
                        ) {
                            outLog.println("PREFIX mismatch. Dropping PREFIX")
                            preFix = ""
                        }
                        break
                    }
                    k++
                }
            }
            if (preFix == "") {
                outLog.println("Unable to determine PREFIX for table")
            }
            proc.lines.insertElementAt(Line("SELECT "), 0)
            j = 0
            while (j < proc.outputs.size) {
                val fieldName = proc.outputs.elementAt(j)
                if (table.hasField(fieldName.name)) {
                    line = if (j == 0) if (preFix.length > 0) "  $preFix." else "  "
                    else if (preFix.length > 0) ", $preFix."
                    else ", "
                } else {
                    fieldName.isExtStd = true
                    fieldName.isExtStdOut = true
                    line = if (j == 0) "  " else ", "
                }
                proc.lines.insertElementAt(Line(line + fieldName.useLiteral(true) + " "), j + 1)
                j++
            }
            if (proc.isStd) {
                proc.isStd = false
                proc.extendsStd = true
                proc.useStd = true
            }
        }
    }

    override fun toString(): String {
        return name
    }

    private operator fun set(a: String, b: String, what: String, outLog: PrintWriter): String {
        var a = a
        if (a.length == 0) a = b
        else if (a.equals(
                b,
                ignoreCase = true
            ) == false
        ) outLog.println("Import $what name :$a not the same as :$b")
        return a
    }

    private operator fun set(a: Boolean, b: Boolean, what: String, outLog: PrintWriter): Boolean {
        var a = a
        if (a == false) a = b
        else if (b == false) outLog.println("Import $what is already true and is not set to false.")
        return a
    }

    private fun copy(addin: Table, outLog: PrintWriter) {
        name = addin.name
        alias = addin.alias
        check = addin.check
        fields = addin.fields
        keys = addin.keys
        links = addin.links
        grants = addin.grants
        views = addin.views
        procs = addin.procs
        comments = addin.comments
        options = addin.options
        allUsers = addin.allUsers
        hasPrimaryKey = addin.hasPrimaryKey
        hasSequence = addin.hasSequence
        hasTimeStamp = addin.hasTimeStamp
        hasAutoTimeStamp = addin.hasAutoTimeStamp
        hasUserStamp = addin.hasUserStamp
        hasExecute = addin.hasExecute
        hasSelect = addin.hasSelect
        hasInsert = addin.hasInsert
        hasDelete = addin.hasDelete
        hasUpdate = addin.hasUpdate
        hasStdProcs = addin.hasStdProcs
        hasIdentity = addin.hasIdentity
        start = addin.start
    }

    private fun merge(addin: Table, outLog: PrintWriter) {
        alias = set(alias, addin.alias, "alias", outLog)
        check = set(check, addin.check, "check", outLog)
        hasPrimaryKey = set(hasPrimaryKey, addin.hasPrimaryKey, "hasPrimaryKey", outLog)
        hasSequence = set(hasSequence, addin.hasSequence, "hasSequence", outLog)
        hasTimeStamp = set(hasTimeStamp, addin.hasTimeStamp, "hasTimeStamp", outLog)
        hasAutoTimeStamp = set(hasAutoTimeStamp, addin.hasAutoTimeStamp, "hasAutoTimeStamp", outLog)
        hasUserStamp = set(hasUserStamp, addin.hasUserStamp, "hasUserStamp", outLog)
        hasExecute = set(hasExecute, addin.hasExecute, "hasExecute", outLog)
        hasSelect = set(hasSelect, addin.hasSelect, "hasSelect", outLog)
        hasInsert = set(hasInsert, addin.hasInsert, "hasInsert", outLog)
        hasDelete = set(hasDelete, addin.hasDelete, "hasDelete", outLog)
        hasUpdate = set(hasUpdate, addin.hasUpdate, "hasUpdate", outLog)
        hasStdProcs = set(hasStdProcs, addin.hasStdProcs, "hasStdProcs", outLog)
        hasIdentity = set(hasIdentity, addin.hasIdentity, "hasIdentity", outLog)
    }

    fun add(addin: Table, outLog: PrintWriter): Table {
        val table = Table()
        table.copy(this, outLog)
        table.merge(addin, outLog)
        return table
    }

    fun hasOption(value: String): Boolean {
        for (i in options.indices) {
            val option = options.elementAt(i)
            if (option!!.lowercase(Locale.getDefault())
                    .compareTo(value.lowercase(Locale.getDefault())) == 0
            ) return true
        }
        return false
    }

    companion object {
        private const val serialVersionUID = 1L
        fun isIdentity(field: Field?): Boolean {
            return field!!.type == Field.BIGIDENTITY || field.type == Field.IDENTITY
        }

        fun isSequence(field: Field?): Boolean {
            return field!!.type == Field.BIGSEQUENCE || field.type == Field.SEQUENCE
        }

        /**
         * Translates field type to DB2 SQL column types
         */
        fun varType(field: Field): String {
            when (field.type) {
                Field.BYTE -> return "SMALLINT"
                Field.SHORT -> return "SMALLINT"
                Field.INT, Field.SEQUENCE, Field.IDENTITY -> return "INT"
                Field.LONG, Field.BIGSEQUENCE, Field.BIGIDENTITY -> return "BIGINT"
                Field.CHAR -> return if (field.length > 32762) "CLOB(" + field.length + ")" else "VARCHAR(" + field.length + ")"
                Field.ANSICHAR -> return "CHAR(" + field.length + ")"
                Field.DATE -> return "DATE"
                Field.DATETIME -> return "TIMESTAMP"
                Field.TIME -> return "TIME"
                Field.TIMESTAMP, Field.AUTOTIMESTAMP -> return "TIMESTAMP"
                Field.FLOAT, Field.DOUBLE -> {
                    if (field.scale != 0) return "DECIMAL(" + field.precision + ", " + field.scale + ")" else if (field.precision != 0) return "DECIMAL(" + field.precision + ", 0)"
                    return "DOUBLE"
                }
                Field.BLOB -> return "BLOB(" + field.length + ")"
                Field.TLOB -> return "CLOB(" + field.length + ")"
                Field.MONEY -> return "DECIMAL(18,2)"
                Field.USERSTAMP -> return "VARCHAR(50)"
                Field.XML -> return "XML"
            }
            return "unknown"
        }
    }

    init {
        fields = Vector<Field?>()
        keys = Vector<Key?>()
        links = Vector<Link?>()
        grants = Vector<Grant?>()
        views = Vector<View?>()
        procs = Vector<Proc?>()
        withs = Vector<With?>()
        comments = Vector<String?>()
        options = Vector<String?>()
        allUsers = Vector<Any?>()
        parameters = Vector<Any?>()
        consts = Vector<Any?>()
        hasExecute = false
        hasSelect = false
        hasInsert = false
        hasDelete = false
        hasUpdate = false
        hasPrimaryKey = false
        hasSequence = false
        hasTimeStamp = false
        hasAutoTimeStamp = false
        hasUserStamp = false
        hasStdProcs = false
        hasIdentity = false
        hasSequenceReturning = false
        hasBigXML = false
        isStoredProc = false
        isLiteral = false
        start = 0
    }
}