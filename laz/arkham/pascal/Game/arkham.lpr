program arkham;

{$mode objfpc}{$H+}

uses
  {$IFDEF UNIX}{$IFDEF UseCThreads}
  cthreads,
  {$ENDIF}{$ENDIF}
  Interfaces, // this includes the LCL widgetset
  Forms, MainUnit, AHGame, AHTypes, AHGamePieces, InvestigatorUnit,
  ChooseInvestigatorsUnit, RevealAncientOneUnit, ActionsFrameUnit, 
chooseexpansionsunit, ahlogger;

{$R *.res}

begin
  RequireDerivedFormResource := True;
  Application.Initialize;
  Application.CreateForm(TMainForm, MainForm);
  Application.CreateForm(TChooseExpansionsForm, ChooseExpansionsForm);
  Application.Run;
end.

