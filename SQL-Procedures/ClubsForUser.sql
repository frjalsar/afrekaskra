USE [Athletics]
GO
/****** Object:  StoredProcedure [dbo].[ClubsForUser]    Script Date: 5/5/2021 8:28:22 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
ALTER PROCEDURE [dbo].[ClubsForUser]
  @UserLogin nvarchar(50)

AS
BEGIN
	SET NOCOUNT ON;

	DECLARE @ClubsForUsr TABLE (
	  Club nvarchar(10),
	  NameOfClub nvarchar(100),
	  Héraðssamband nvarchar(10),
	  NoOfMembers int);

	DECLARE @NoOfClubs int;
	SET @NoOfClubs = (SELECT COUNT(*) FROM Athl$UserAccessClubs WHERE UserName = @UserLogin);
	IF @NoOfClubs = 0 BEGIN 
	  SELECT Félag as Club, Félag + ' - ' + [Heiti félags] as NameOfClub, Héraðssamband FROM Athl$Clubs where Tegund in (1,2,3,8,9)  order by Club
	END
	ELSE BEGIN
      DECLARE @CompetitonsInNearFuture TABLE (
	    CompetitionCode nvarchar(20));
	  INSERT INTO @CompetitonsInNearFuture (CompetitionCode)
	    SELECT Code FROM Athl$Competition WHERE CompetitonType = 1 AND [Date] BETWEEN GETDATE() - 1 AND GETDATE() + 9;	  
	  INSERT INTO @ClubsForUsr (Club, NameOfClub, Héraðssamband) --, NoOfMembers)
  	  SELECT UserAcc.Club, Club + ' - ' +  (SELECT [Heiti félags] FROM Athl$Clubs WHERE Félag = UserAcc.Club), 
	    (SELECT Héraðssamband FROM Athl$Clubs WHERE Félag = UserAcc.Club)
--		(SELECT COUNT(*) FROM Athl$Competitors WHERE Félag = UserAcc.Club)
        FROM Athl$UserAccessClubs UserAcc WHERE UserName = @UserLogin;
	  UPDATE @ClubsForUsr 
	    SET NoOfMembers = (
		    SELECT COUNT(*) FROM Athl$CompetitorsInCompetition AthlCompInC 
			  WHERE mot IN (SELECT CompetitionCode FROM @CompetitonsInNearFuture) AND AthlCompInC.felag = Club)

      SELECT Club, NameOfClub, Héraðssamband FROM @ClubsForUsr ORDER BY NoOfMembers DESC;
	END


END
