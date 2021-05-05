USE [Athletics]
GO
/****** Object:  StoredProcedure [dbo].[CompetitorsRecords]    Script Date: 5/5/2021 8:30:04 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[CompetitorsRecords]
  @CompetitorNo nvarchar(20),
  @YearFrom int,
  @YearTo int,
  @OutdoorsIndoorsFilter nvarchar(10)
AS
BEGIN

  SET NOCOUNT ON;

  DECLARE @Records TABLE (
    LineType int,
	ActiveText nvarchar(20),
	AgeGroup nvarchar(30),
	EventName nvarchar(100),
	OutdoorsOrIndoors nvarchar(10),
	Results nvarchar(20),
    AchievementDate datetime,
	Venue nvarchar(50),
	Club nvarchar(20),
	Age int,
	WindReading decimal(38,20),
	CompetitionName nvarchar(50),
	CompetitionCode nvarchar(20),
	Placing nvarchar(10),
	Remarks nvarchar(100));

INSERT INTO @Records (LineType, ActiveText, AgeGroup, EventName, OutdoorsOrIndoors, Results,
  AchievementDate, Venue, Club, Age, WindReading, CompetitionName, CompetitionCode, Placing, Remarks)
  SELECT 1, 
    CASE WHEN Virkt = 1 THEN 'Virkt' ELSE 'Óvirkt' END,
    [Aldursflokkur FRÍ], (SELECT TOP 1 Heiti FROM  Athl$Events WHERE Grein = Recs.Grein 
    AND Kyn = Recs.Kyn AND Flokkur = Recs.Flokkur AND Úti_Inni = Recs.Úti_Inni) as HeitiGr, 
	CASE WHEN Úti_Inni = 0 THEN 'Úti' ELSE 'Inni' END, Árangur, [Dagsetning mets], [Staður mets], 
	[Félag methafa], [Aldur methafa], Vindur,
	(SELECT [Heiti Móts] FROM Athl$Afrek WHERE Lína = Recs.[Línunr_ í afrekum]) as CompetitionName,
	(SELECT [Mót] FROM Athl$Afrek WHERE Lína = Recs.[Línunr_ í afrekum]) as CompetitionCode,
	(SELECT Röð FROM Athl$Afrek WHERE Lína = Recs.[Línunr_ í afrekum]) as Place,
	Athugasemd	
    FROM [Athl$Metaskrá FRÍ] Recs WHERE Methafi = @CompetitorNo AND
	  DATEPART(Year, [Dagsetning mets]) >= @YearFrom AND
	  DATEPART(Year, [Dagsetning mets]) <= @YearTo AND
	  Úti_Inni LIKE @OutdoorsIndoorsFilter;

SELECT * FROM @Records;    

END
