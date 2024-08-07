USE [Athletics]
GO
/****** Object:  StoredProcedure [dbo].[CompetitorsAchievementsSif]    Script Date: 9/17/2022 1:37:29 PM ******/
/****** Breytt útgáfa af CompetitorsAchievements ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[CompetitorsAchievementsSif]
  @CompetitorNo nvarchar(20),
  @YearFrom int,
  @YearTo int,
  @OutdoorsIndoorsFilter nvarchar(10)
AS
BEGIN

  SET NOCOUNT ON;
--DECLARE @CompetitorNo nvarchar(10);
--DECLARE @YearFrom int;
--DECLARE @YearTo int;
--DECLARE @OutdoorsIndoorsFilter nvarchar(10);

--set @CompetitorNo = '2504'; --//'103750';
--set @YearFrom = 1800;
--set @YearTo = 2015;
--set @OutdoorsIndoorsFilter = '%';
 DECLARE @AchieveMents TABLE (
	EventName nvarchar(100),
	OutdoorsOrIndoors nvarchar(10),
	Results nvarchar(250),
    AchievementDate datetime,
	Venue nvarchar(50),
	Club nvarchar(20),
	Age int,
	WindReading decimal(38,1),
	CompetitionName nvarchar(50),
	CompetitionCode nvarchar(20),
	Placing nvarchar(10),
	Remarks nvarchar(200),
	Rafmagnstímataka int,
	EventSortOrder decimal(38,20),
	AchievementSortOrder decimal(30,20),
	Series nvarchar(150),
	RequiresWindMeter int,
	WindReadingText nvarchar(20));

INSERT INTO @AchieveMents (EventName, OutdoorsOrIndoors, Results,
  AchievementDate, Venue, Club, Age, WindReading, CompetitionName, CompetitionCode, Placing, Remarks, 
  Rafmagnstímataka, EventSortOrder, AchievementSortOrder, Series, RequiresWindMeter, WindReadingText)
  SELECT (SELECT TOP 1 Heiti FROM  Athl$Events WHERE Grein = Afr.Grein 
    AND Kyn = Afr.Kyn AND Flokkur = Afr.Flokkur AND Úti_Inni = Afr.Úti_Inni) as HeitiGr, 
	CASE WHEN Úti_Inni = 0 THEN 'Úti' ELSE 'Inni' END, Árangur + ' ' + Athugasemd, Dagsetning, Staður, 
	Félag, [Aldur keppanda], Vindur, [Heiti Móts], [Mót], [Röð], [Athugasemd], Rafmagnstímataka, 
	(SELECT [Röð í afrekaskrá] FROM Athl$Events WHERE Grein = Afr.Grein 
    AND Kyn = Afr.Kyn AND Flokkur = Afr.Flokkur AND Úti_Inni = Afr.Úti_Inni) as EventSortOrd,
	Raðsvæði, Sería,
	(SELECT TOP 1 [Krefst vindmælis] FROM Athl$Events AEv WHERE AEv.Grein = Afr.Grein AND AEv.Kyn = Afr.Kyn AND AEv.Flokkur = Afr.Flokkur AND AEv.Úti_Inni = Afr.Úti_Inni),
	''
  FROM [Athl$Afrek] Afr WHERE Keppandanúmer = @CompetitorNo AND
  	  DATEPART(Year, [Dagsetning]) >= @YearFrom AND
	  DATEPART(Year, [Dagsetning]) <= @YearTo AND
	  Úti_Inni LIKE @OutdoorsIndoorsFilter; 

UPDATE @AchieveMents 
  SET WindReadingText = CONVERT(NVARCHAR(20), WindReading) 
  WHERE RequiresWindMeter = 1;
UPDATE @AchieveMents
  SET WindReadingText = '+' + WindReadingText 
  WHERE RequiresWindMeter = 1 AND WindReading >= 0;
  
SELECT * FROM @AchieveMents ORDER by EventSortOrder, AchievementSortOrder, AchievementDate    
END;