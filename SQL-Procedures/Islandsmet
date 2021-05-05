USE [Athletics]
GO
/****** Object:  StoredProcedure [dbo].[Islandsmet]    Script Date: 5/5/2021 8:29:27 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[Islandsmet]
AS
BEGIN
	SET NOCOUNT ON;
	DECLARE @Metaskra table (
	  LineType int,
	  AldursflFRÍ nvarchar(10),
	  AldurTil int,
	  Gr nvarchar(10),
	  Ky int,
	  Fl nvarchar(10),
	  ÚtiInni int,
      HeitiGreinar nvarchar(100),
	  Arangur nvarchar(30),
	  Vindur nvarchar(10),
	  Nafn nvarchar(50),
	  Félag nvarchar(10),
	  Staður nvarchar(50),
	  Dagsetn date,
	  RöðÍAfrekaskrá decimal(38,20),
	  KrefsVindm int,
	  Keppandan nvarchar(10),
	  FyrriMetLinkur nvarchar(100));

	 INSERT INTO @Metaskra (LineType, AldursflFRÍ, Gr, Ky, Fl, ÚtiInni, HeitiGreinar, Arangur, Vindur, 
	   Nafn, Félag, Staður, Dagsetn, RöðÍAfrekaskrá, Keppandan, FyrriMetLinkur)
	 SELECT 2, [Aldursflokkur FRÍ], Grein, Kyn, Flokkur, Úti_Inni, '', Árangur + ' ' + Athugasemd, [dbo].[ReturnWindText](Vindur),
	   [Heiti methafa] + ' (' + CONVERT(nvarchar(4),[Fæðingarár methafa]) + ')',  [Félag methafa], [Staður mets], [Dagsetning mets], [Röð í afrekaskrá], Methafi,
	    '' FROM [Athl$Metaskrá FRÍ]
	   where Virkt = 1
   update @Metaskra
     set HeitiGreinar = (SELECT TOP 1 Heiti FROM Athl$Events Grn WHERE Grn.Grein = Gr AND Grn.Kyn = Ky AND Grn.Flokkur = Fl AND
	   Grn.Úti_Inni = Úti_Inni) WHERE LineType = 2;
   update @Metaskra 
     SET AldurTil = (SELECT TOP 1 [Aldur Til] from [Athl$Aldursflokkar FRÍ] AldFRI WHERE AldFRI.Tákn = AldursflFRÍ);
   update @Metaskra
     set KrefsVindm = (SELECT TOP 1 [Krefst vindmælis] FROM Athl$Events Grx WHERE Grx.Grein = Gr AND Grx.Kyn = Ky AND Grx.Flokkur = Fl AND
	   Grx.Úti_Inni = ÚtiInni) WHERE LineType = 2;  
   UPDATE @Metaskra 
     SET Vindur = '' WHERE KrefsVindm = 0 OR Vindur = '+0,0'
   INSERT INTO @Metaskra (LineType, ÚtiInni, AldursflFRÍ, HeitiGreinar, AldurTil, Ky, Arangur)
     SELECT 1, 0, Tákn, Heiti, [Aldur Til], Kyn, 'H' From [Athl$Aldursflokkar FRÍ] WHERE [Aldur Til] > 11;	    
   INSERT INTO @Metaskra (LineType, ÚtiInni, AldursflFRÍ, HeitiGreinar, AldurTil, Ky, Arangur)
     SELECT 1, 1, Tákn, Heiti, [Aldur Til], Kyn, 'H' From [Athl$Aldursflokkar FRÍ] WHERE [Aldur Til] > 11; 
	 
   select * from @Metaskra order by ÚtiInni, Ky, AldurTil DESC, LineType, RöðÍAfrekaskrá
END
