unit ChooseExpansionsUnit;
(***
This code uses materials which are the intellectual property of
the Arkham Horror Board Game and expansions.
As such this code cannot be put into the public domain or even
as open source.
***)

{$mode delphi}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, ExtCtrls,
  StdCtrls;

type

  { TChooseExpansionsForm }

  TChooseExpansionsForm = class(TForm)
    COTDPCheckBox: TCheckBox;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    OkButton: TButton;
    TBGOTWCheckBox: TCheckBox;
    Image1: TImage;
    TKIYCheckBox: TCheckBox;
    TLATTCheckBox: TCheckBox;
    procedure FormActivate(Sender: TObject);
    procedure FormCreate(Sender: TObject);
  private
    { private declarations }
    justCreated : boolean;
  public
    { public declarations }
  end;

var
  ChooseExpansionsForm: TChooseExpansionsForm;

implementation

{$R *.lfm}

{ TChooseExpansionsForm }

procedure TChooseExpansionsForm.FormCreate(Sender: TObject);
begin
  justCreated := true;
end;

procedure TChooseExpansionsForm.FormActivate(Sender: TObject);
begin
  if justCreated = false then exit;
  justCreated := false;
end;

end.

