export module audit;
import machine;
import ociapi;
import databuilder;
#define JP_MARK __FILE__, __LINE__

export struct DAudits
{
	int32  Id;
	char   TableName[65];
	char   Action[11];
	char   Old[2001];
	char   New[2001];
	char   USId[17];
	char   TmStamp[15];

	void Clear()
	{
		Id = 0;
		memset(TableName, 0, sizeof(TableName));
		memset(Action, 0, sizeof(Action));
		memset(Old, 0, sizeof(Old));
		memset(New, 0, sizeof(New));
		memset(USId, 0, sizeof(USId));
		memset(TmStamp, 0, sizeof(TmStamp));
	}
	DAudits()
	{
		Clear();
	}
	static int NoBuildFields()
	{
		return 7;
	}
	void _buildAdds(DataBuilder& dBuild)
	{
		dBuild.add("Id", Id);
		dBuild.add("TableName", TableName);
		dBuild.add("Action", Action);
		dBuild.add("Old", Old);
		dBuild.add("New", New);
		dBuild.add("USId", USId);
		dBuild.add("TmStamp", TmStamp);
	}
	void BuildData(DataBuilder& dBuild, const char* name)
	{
		dBuild.name(name);
		_buildAdds(dBuild);
	}
	void BuildData(DataBuilder& dBuild) { BuildData(dBuild, "Audits"); }
	void _buildSets(DataBuilder& dBuild)
	{
		dBuild.set("Id", Id, sizeof(Id));
		dBuild.set("TableName", TableName, sizeof(TableName));
		dBuild.set("Action", Action, sizeof(Action));
		dBuild.set("Old", Old, sizeof(Old));
		dBuild.set("New", New, sizeof(New));
		dBuild.set("USId", USId, sizeof(USId));
		dBuild.set("TmStamp", TmStamp, sizeof(TmStamp));
	}
	void SetData(DataBuilder& dBuild, const char* name)
	{
		dBuild.name(name);
		_buildSets(dBuild);
	}
	void SetData(DataBuilder& dBuild) { SetData(dBuild, "Audits"); }
};

export using OAudits = DAudits;

export struct DAuditsDeleteOne
{
	int32  Id;

	void Clear()
	{
		Id = 0;
	}
	DAuditsDeleteOne()
	{
		Clear();
	}
	static int NoBuildFields()
	{
		return 1;
	}
	void _buildAdds(DataBuilder& dBuild)
	{
		dBuild.add("Id", Id);
	}
	void BuildData(DataBuilder& dBuild, const char* name)
	{
		dBuild.name(name);
		_buildAdds(dBuild);
	}
	void BuildData(DataBuilder& dBuild) { BuildData(dBuild, "AuditsDeleteOne"); }
	void _buildSets(DataBuilder& dBuild)
	{
		dBuild.set("Id", Id, sizeof(Id));
	}
	void SetData(DataBuilder& dBuild, const char* name)
	{
		dBuild.name(name);
		_buildSets(dBuild);
	}
	void SetData(DataBuilder& dBuild) { SetData(dBuild, "AuditsDeleteOne"); }
};

export struct OAuditsExists
{
	int32  noOf;

	void Clear()
	{
		noOf = 0;
	}
	OAuditsExists()
	{
		Clear();
	}
	static int NoBuildFields() { return 1; }
	void _buildAdds(DataBuilder& dBuild)
	{
		dBuild.add("noOf", noOf);
	}
	void BuildData(DataBuilder& dBuild, const char* name)
	{
		dBuild.name(name);
		_buildAdds(dBuild);
	}
	void BuildData(DataBuilder& dBuild) { BuildData(dBuild, "AuditsExists"); }
	void _buildSets(DataBuilder& dBuild)
	{
		dBuild.set("noOf", noOf, sizeof(noOf));
	}
	void SetData(DataBuilder& dBuild, const char* name)
	{
		dBuild.name(name);
		_buildSets(dBuild);
	}
	void SetData(DataBuilder& dBuild) { SetData(dBuild, "AuditsExists"); }
};

export struct DAuditsExists : public OAuditsExists
{
	int32  Id;

	void Clear()
	{
		OAuditsExists::Clear();
		Id = 0;
	}
	DAuditsExists()
	{
		Clear();
	}
	static int NoBuildFields()
	{
		return OAuditsExists::NoBuildFields() + 1;
	}
	void _buildAdds(DataBuilder& dBuild)
	{
		OAuditsExists::_buildAdds(dBuild);
		dBuild.add("Id", Id);
	}
	void BuildData(DataBuilder& dBuild, const char* name)
	{
		dBuild.name(name);
		_buildAdds(dBuild);
	}
	void BuildData(DataBuilder& dBuild) { BuildData(dBuild, "AuditsExists"); }
	void _buildSets(DataBuilder& dBuild)
	{
		OAuditsExists::_buildSets(dBuild);
		dBuild.set("Id", Id, sizeof(Id));
	}
	void SetData(DataBuilder& dBuild, const char* name)
	{
		dBuild.name(name);
		_buildSets(dBuild);
	}
	void SetData(DataBuilder& dBuild) { SetData(dBuild, "AuditsExists"); }
};

export struct TAuditsExists : public DAuditsExists
{
	enum
	{
		NOOF_OFFSET = 0
		, ROWSIZE = (NOOF_OFFSET + sizeof(int32))
		, NOROWS = 1
		, NOBINDS = 1
		, NODEFINES = 1
		, NOOF_POS = 0
	};
	TJQuery q_;
	void Exec();
	void Exec(DAuditsExists& Rec) { *DRec() = Rec; Exec(); }
	void Exec(
		int32  aId
	);
	bool Fetch();
	TAuditsExists(TJConnector& conn, const char* aFile = __FILE__, long aLine = __LINE__)
		: q_(conn)
	{
		Clear(); q_.FileAndLine(aFile, aLine);
	}
	DAuditsExists* DRec() { return this; }
	OAuditsExists* ORec() { return this; }
};

void TAuditsExists::Exec()
{
	size_t size = 59;
	if (q_.command != 0) delete[] q_.command;
	q_.command = new char[size];
	memset(q_.command, 0, size);
	strcat(q_.command, "select count(*) noOf from DBUD00.Audits""\n"
		" where Id = :Id");
	q_.Open(q_.command, NOBINDS, NODEFINES, NOROWS, ROWSIZE);
	q_.Bind(":Id", 0, Id);
	q_.Define(0, (int32*)(q_.data + NOOF_POS));
	q_.Exec();
}

void TAuditsExists::Exec(
	int32  aId
)
{
	Id = aId;
	Exec();
}

bool TAuditsExists::Fetch()
{
	if (q_.Fetch() == false)
		return false;
	q_.Get(noOf, q_.data + NOOF_POS);
	return true;
}

export bool AuditsExists(TJConnector* connect, DAuditsExists* rec)
{
	TAuditsExists q(*connect, JP_MARK);
	q.Exec(*rec);
	if (q.Fetch())
	{
		*rec = *q.DRec();
		return true;
	}
	return false;
}


