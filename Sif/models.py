# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class NdoDbproperty(models.Model):
    programid = models.IntegerField()
    chartable = models.BinaryField(blank=True, null=True)
    maxrecsize = models.IntegerField()
    maxloginattempts = models.IntegerField()
    passwordexpindays = models.IntegerField()
    supergroupid = models.CharField(max_length=128)
    unifiedloginallowed = models.SmallIntegerField()
    contype = models.IntegerField()
    shadowpwd = models.CharField(max_length=128)
    databasemagic = models.IntegerField()
    databaseversionno = models.IntegerField()
    clientdatabaseversionno = models.IntegerField()
    maintainviews = models.IntegerField()
    diagnostics = models.IntegerField()
    identifiers = models.CharField(max_length=2000)
    maintainrelationships = models.IntegerField()
    convertidentifiers = models.IntegerField()
    invalididentifierchars = models.CharField(max_length=128)
    license = models.BinaryField(blank=True, null=True)
    checkcodepage = models.IntegerField()
    quickfind = models.IntegerField()
    maintaindefaults = models.IntegerField()
    locktimeout = models.IntegerField()
    locktimeoutperiod = models.IntegerField()
    hardrowlock = models.IntegerField()
    bufferedrows = models.IntegerField()
    securityoption = models.IntegerField()
    enabledforserver = models.IntegerField()

    class Meta:
        managed = False
        db_table = '$ndo$dbproperty'


class AthlActionCounters(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    code = models.CharField(db_column='Code', primary_key=True, max_length=10)  # Field name made lowercase.
    action_selected = models.IntegerField(db_column='Action Selected')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    action_commited = models.IntegerField(db_column='Action Commited')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Action Counters'


class AthlActions(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entry_no_field = models.IntegerField(db_column='Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    replication_counter = models.IntegerField(db_column='Replication Counter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_group_filter = models.CharField(db_column='Location Group Filter', max_length=21)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    action = models.IntegerField(db_column='Action')  # Field name made lowercase.
    table_no_field = models.IntegerField(db_column='Table No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    key = models.CharField(db_column='Key', max_length=250)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    user_id = models.CharField(db_column='User ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    batchid = models.CharField(db_column='BatchID', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Actions'
        unique_together = (('table_no_field', 'entry_no_field', 'location_group_filter'), ('date', 'table_no_field', 'entry_no_field'),)


class AthlActionsFrj(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entry_no_field = models.IntegerField(db_column='Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    source_counter = models.IntegerField(db_column='Source Counter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_group_filter = models.CharField(db_column='Location Group Filter', max_length=21)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    action = models.IntegerField(db_column='Action')  # Field name made lowercase.
    table_no_field = models.IntegerField(db_column='Table No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    key = models.CharField(db_column='Key', max_length=250)  # Field name made lowercase.
    date_created = models.DateTimeField(db_column='Date Created')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    time_created = models.DateTimeField(db_column='Time Created')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_id = models.CharField(db_column='User ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pos_terminal_key = models.CharField(db_column='POS Terminal Key', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    move_action = models.SmallIntegerField(db_column='Move Action')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    table_in_blob = models.IntegerField(db_column='Table in Blob')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Actions FRJ'
        unique_together = (('table_no_field', 'date_created', 'entry_no_field'),)


class AthlAfrek(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    raðsvæði = models.DecimalField(db_column='Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=10)  # Field name made lowercase.
    vindur = models.DecimalField(db_column='Vindur', max_digits=38, decimal_places=20)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    metrar = models.DecimalField(db_column='Metrar', max_digits=38, decimal_places=20)  # Field name made lowercase.
    tími = models.CharField(db_column='Tími', max_length=10)  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    löglegt = models.SmallIntegerField(db_column='Löglegt')  # Field name made lowercase.
    röð = models.CharField(db_column='Röð', max_length=10)  # Field name made lowercase.
    rafmagnstímataka = models.SmallIntegerField(db_column='Rafmagnstímataka')  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    aldur_keppanda = models.IntegerField(db_column='Aldur keppanda')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mót = models.CharField(db_column='Mót', max_length=10)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    heiti_móts = models.CharField(db_column='Heiti Móts', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sería = models.CharField(db_column='Sería', max_length=150)  # Field name made lowercase.
    athugasemd = models.CharField(db_column='Athugasemd', max_length=125)  # Field name made lowercase.
    röð_í_afrekaskrá_ársins = models.IntegerField(db_column='Röð í afrekaskrá ársins')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_í_afrekaskrá_flokksins = models.IntegerField(db_column='Röð í afrekaskrá flokksins')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    riðill = models.IntegerField(db_column='Riðill')  # Field name made lowercase.
    félag_innan_sambands = models.CharField(db_column='Félag innan sambands', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_vind = models.SmallIntegerField(db_column='Vantar vind')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    erlendur_ríkisborgari = models.SmallIntegerField(db_column='Erlendur ríkisborgari')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ekki_í_afrekaskrá = models.SmallIntegerField(db_column='Ekki í afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tegund_móts = models.IntegerField(db_column='Tegund móts')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    riðill_númer = models.IntegerField(db_column='Riðill númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grein_númer = models.IntegerField(db_column='Grein númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_innan_greinar = models.IntegerField(db_column='Röð innan greinar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keppnisgreinar_móts_lína = models.IntegerField(db_column='Keppnisgreinar móts lína')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_dag_og_mánuð = models.SmallIntegerField(db_column='Vantar dag og mánuð')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldursflokkur_öldunga = models.CharField(db_column='Aldursflokkur öldunga', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_greinar = models.CharField(db_column='Tákn Greinar', max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldursflokkur_frí = models.CharField(db_column='Aldursflokkur FRÍ', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metaupplýsingar = models.CharField(db_column='Metaupplýsingar', max_length=50)  # Field name made lowercase.
    sama_afrek_tvisvar = models.SmallIntegerField(db_column='Sama afrek tvisvar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uppfært_á_fri_is = models.SmallIntegerField(db_column='Uppfært á FRI_IS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    replication_counter = models.IntegerField(db_column='Replication Counter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kóti_tegund_móts = models.CharField(db_column='Kóti Tegund Móts', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    additional_info = models.CharField(db_column='Additional Info', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stig = models.DecimalField(db_column='Stig', max_digits=38, decimal_places=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Afrek'
        unique_together = (('úti_inni', 'kyn', 'grein', 'flokkur', 'raðsvæði', 'dagsetning', 'riðill', 'röð_innan_greinar', 'lína'), ('keppandanúmer', 'grein', 'flokkur', 'úti_inni', 'raðsvæði', 'dagsetning', 'lína'), ('heiti_móts', 'dagsetning', 'grein', 'lína'), ('mót', 'kyn', 'grein', 'flokkur', 'raðsvæði', 'röð_innan_greinar', 'lína'), ('mót', 'kyn', 'flokkur', 'lína'), ('tegund_móts', 'úti_inni', 'kyn', 'grein', 'flokkur', 'raðsvæði', 'dagsetning', 'riðill', 'röð', 'lína'), ('mót', 'grein_númer', 'raðsvæði', 'röð_innan_greinar', 'röð', 'lína'), ('aldursflokkur_öldunga', 'úti_inni', 'kyn', 'grein', 'flokkur', 'raðsvæði', 'dagsetning', 'riðill', 'röð_innan_greinar', 'lína'), ('replication_counter', 'lína'), ('félag', 'keppandanúmer', 'dagsetning', 'lína'),)


class AthlAfrekGunnarJ(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    raðsvæði = models.DecimalField(db_column='Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=10)  # Field name made lowercase.
    vindur = models.DecimalField(db_column='Vindur', max_digits=38, decimal_places=20)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    metrar = models.DecimalField(db_column='Metrar', max_digits=38, decimal_places=20)  # Field name made lowercase.
    tími = models.CharField(db_column='Tími', max_length=10)  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    löglegt = models.SmallIntegerField(db_column='Löglegt')  # Field name made lowercase.
    röð = models.CharField(db_column='Röð', max_length=10)  # Field name made lowercase.
    rafmagnstímataka = models.SmallIntegerField(db_column='Rafmagnstímataka')  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    aldur_keppanda = models.IntegerField(db_column='Aldur keppanda')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mót = models.CharField(db_column='Mót', max_length=10)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    heiti_móts = models.CharField(db_column='Heiti Móts', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sería = models.CharField(db_column='Sería', max_length=80)  # Field name made lowercase.
    athugasemd = models.CharField(db_column='Athugasemd', max_length=30)  # Field name made lowercase.
    röð_í_afrekaskrá_ársins = models.IntegerField(db_column='Röð í afrekaskrá ársins')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_í_afrekaskrá_flokksins = models.IntegerField(db_column='Röð í afrekaskrá flokksins')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    riðill = models.IntegerField(db_column='Riðill')  # Field name made lowercase.
    félag_innan_sambands = models.CharField(db_column='Félag innan sambands', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_vind = models.SmallIntegerField(db_column='Vantar vind')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    erlendur_ríkisborgari = models.SmallIntegerField(db_column='Erlendur ríkisborgari')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ekki_í_afrekaskrá = models.SmallIntegerField(db_column='Ekki í afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Afrek Gunnar Jó'
        unique_together = (('úti_inni', 'kyn', 'grein', 'flokkur', 'raðsvæði', 'dagsetning', 'riðill', 'röð', 'lína'), ('keppandanúmer', 'grein', 'flokkur', 'úti_inni', 'raðsvæði', 'dagsetning', 'lína'), ('heiti_móts', 'dagsetning', 'grein', 'lína'), ('athugasemd', 'lína'), ('mót', 'kyn', 'flokkur', 'lína'),)


class AthlAfrekTest(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    raðsvæði = models.DecimalField(db_column='Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=10)  # Field name made lowercase.
    vindur = models.DecimalField(db_column='Vindur', max_digits=38, decimal_places=20)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    metrar = models.DecimalField(db_column='Metrar', max_digits=38, decimal_places=20)  # Field name made lowercase.
    tími = models.CharField(db_column='Tími', max_length=10)  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    löglegt = models.SmallIntegerField(db_column='Löglegt')  # Field name made lowercase.
    röð = models.CharField(db_column='Röð', max_length=10)  # Field name made lowercase.
    rafmagnstímataka = models.SmallIntegerField(db_column='Rafmagnstímataka')  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    aldur_keppanda = models.IntegerField(db_column='Aldur keppanda')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mót = models.CharField(db_column='Mót', max_length=10)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    heiti_móts = models.CharField(db_column='Heiti Móts', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sería = models.CharField(db_column='Sería', max_length=100)  # Field name made lowercase.
    athugasemd = models.CharField(db_column='Athugasemd', max_length=125)  # Field name made lowercase.
    röð_í_afrekaskrá_ársins = models.IntegerField(db_column='Röð í afrekaskrá ársins')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_í_afrekaskrá_flokksins = models.IntegerField(db_column='Röð í afrekaskrá flokksins')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    riðill = models.IntegerField(db_column='Riðill')  # Field name made lowercase.
    félag_innan_sambands = models.CharField(db_column='Félag innan sambands', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_vind = models.SmallIntegerField(db_column='Vantar vind')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    erlendur_ríkisborgari = models.SmallIntegerField(db_column='Erlendur ríkisborgari')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ekki_í_afrekaskrá = models.SmallIntegerField(db_column='Ekki í afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tegund_móts = models.IntegerField(db_column='Tegund móts')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    riðill_númer = models.IntegerField(db_column='Riðill númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grein_númer = models.IntegerField(db_column='Grein númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_innan_greinar = models.IntegerField(db_column='Röð innan greinar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keppnisgreinar_móts_lína = models.IntegerField(db_column='Keppnisgreinar móts lína')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_dag_og_mánuð = models.SmallIntegerField(db_column='Vantar dag og mánuð')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldursflokkur_öldunga = models.CharField(db_column='Aldursflokkur öldunga', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_greinar = models.CharField(db_column='Tákn Greinar', max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldursflokkur_frí = models.CharField(db_column='Aldursflokkur FRÍ', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metaupplýsingar = models.CharField(db_column='Metaupplýsingar', max_length=50)  # Field name made lowercase.
    sama_afrek_tvisvar = models.SmallIntegerField(db_column='Sama afrek tvisvar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uppfært_á_fri_is = models.SmallIntegerField(db_column='Uppfært á FRI_IS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    replication_counter = models.IntegerField(db_column='Replication Counter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kóti_tegund_móts = models.CharField(db_column='Kóti Tegund Móts', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Afrek TEST'
        unique_together = (('úti_inni', 'kyn', 'grein', 'flokkur', 'raðsvæði', 'dagsetning', 'riðill', 'röð_innan_greinar', 'lína'), ('keppandanúmer', 'grein', 'flokkur', 'úti_inni', 'raðsvæði', 'dagsetning', 'lína'), ('heiti_móts', 'dagsetning', 'grein', 'lína'), ('mót', 'kyn', 'grein', 'flokkur', 'raðsvæði', 'röð_innan_greinar', 'lína'), ('mót', 'kyn', 'flokkur', 'lína'), ('tegund_móts', 'úti_inni', 'kyn', 'grein', 'flokkur', 'raðsvæði', 'dagsetning', 'riðill', 'röð', 'lína'), ('mót', 'grein_númer', 'raðsvæði', 'röð_innan_greinar', 'röð', 'lína'), ('aldursflokkur_öldunga', 'úti_inni', 'kyn', 'grein', 'flokkur', 'raðsvæði', 'dagsetning', 'riðill', 'röð_innan_greinar', 'lína'), ('replication_counter', 'lína'), ('félag', 'keppandanúmer', 'dagsetning', 'lína'),)


class AthlAfrekMeIaafStigum(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    raðsvæði = models.DecimalField(db_column='Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=10)  # Field name made lowercase.
    vindur = models.DecimalField(db_column='Vindur', max_digits=38, decimal_places=20)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    metrar = models.DecimalField(db_column='Metrar', max_digits=38, decimal_places=20)  # Field name made lowercase.
    tími = models.CharField(db_column='Tími', max_length=10)  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    löglegt = models.SmallIntegerField(db_column='Löglegt')  # Field name made lowercase.
    röð = models.CharField(db_column='Röð', max_length=10)  # Field name made lowercase.
    rafmagnstímataka = models.SmallIntegerField(db_column='Rafmagnstímataka')  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    aldur_keppanda = models.IntegerField(db_column='Aldur keppanda')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mót = models.CharField(db_column='Mót', max_length=10)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    heiti_móts = models.CharField(db_column='Heiti Móts', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sería = models.CharField(db_column='Sería', max_length=100)  # Field name made lowercase.
    athugasemd = models.CharField(db_column='Athugasemd', max_length=125)  # Field name made lowercase.
    röð_í_afrekaskrá_ársins = models.IntegerField(db_column='Röð í afrekaskrá ársins')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_í_afrekaskrá_flokksins = models.IntegerField(db_column='Röð í afrekaskrá flokksins')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    riðill = models.IntegerField(db_column='Riðill')  # Field name made lowercase.
    félag_innan_sambands = models.CharField(db_column='Félag innan sambands', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_vind = models.SmallIntegerField(db_column='Vantar vind')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    erlendur_ríkisborgari = models.SmallIntegerField(db_column='Erlendur ríkisborgari')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ekki_í_afrekaskrá = models.SmallIntegerField(db_column='Ekki í afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tegund_móts = models.IntegerField(db_column='Tegund móts')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    riðill_númer = models.IntegerField(db_column='Riðill númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grein_númer = models.IntegerField(db_column='Grein númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_innan_greinar = models.IntegerField(db_column='Röð innan greinar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keppnisgreinar_móts_lína = models.IntegerField(db_column='Keppnisgreinar móts lína')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_dag_og_mánuð = models.SmallIntegerField(db_column='Vantar dag og mánuð')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldursflokkur_öldunga = models.CharField(db_column='Aldursflokkur öldunga', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_greinar = models.CharField(db_column='Tákn Greinar', max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldursflokkur_frí = models.CharField(db_column='Aldursflokkur FRÍ', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metaupplýsingar = models.CharField(db_column='Metaupplýsingar', max_length=50)  # Field name made lowercase.
    sama_afrek_tvisvar = models.SmallIntegerField(db_column='Sama afrek tvisvar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uppfært_á_fri_is = models.SmallIntegerField(db_column='Uppfært á FRI_IS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    replication_counter = models.IntegerField(db_column='Replication Counter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kóti_tegund_móts = models.CharField(db_column='Kóti Tegund Móts', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Afrek með IAAF Stigum'
        unique_together = (('úti_inni', 'kyn', 'raðsvæði', 'lína'),)


class AthlAfrekMeldungastigum(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    raðsvæði = models.DecimalField(db_column='Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=10)  # Field name made lowercase.
    vindur = models.DecimalField(db_column='Vindur', max_digits=38, decimal_places=20)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    metrar = models.DecimalField(db_column='Metrar', max_digits=38, decimal_places=20)  # Field name made lowercase.
    tími = models.CharField(db_column='Tími', max_length=10)  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    löglegt = models.SmallIntegerField(db_column='Löglegt')  # Field name made lowercase.
    röð = models.CharField(db_column='Röð', max_length=10)  # Field name made lowercase.
    rafmagnstímataka = models.SmallIntegerField(db_column='Rafmagnstímataka')  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    aldur_keppanda = models.IntegerField(db_column='Aldur keppanda')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mót = models.CharField(db_column='Mót', max_length=10)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    heiti_móts = models.CharField(db_column='Heiti Móts', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sería = models.CharField(db_column='Sería', max_length=100)  # Field name made lowercase.
    athugasemd = models.CharField(db_column='Athugasemd', max_length=125)  # Field name made lowercase.
    röð_í_afrekaskrá_ársins = models.IntegerField(db_column='Röð í afrekaskrá ársins')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_í_afrekaskrá_flokksins = models.IntegerField(db_column='Röð í afrekaskrá flokksins')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    riðill = models.IntegerField(db_column='Riðill')  # Field name made lowercase.
    félag_innan_sambands = models.CharField(db_column='Félag innan sambands', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_vind = models.SmallIntegerField(db_column='Vantar vind')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    erlendur_ríkisborgari = models.SmallIntegerField(db_column='Erlendur ríkisborgari')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ekki_í_afrekaskrá = models.SmallIntegerField(db_column='Ekki í afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tegund_móts = models.IntegerField(db_column='Tegund móts')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    riðill_númer = models.IntegerField(db_column='Riðill númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grein_númer = models.IntegerField(db_column='Grein númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_innan_greinar = models.IntegerField(db_column='Röð innan greinar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keppnisgreinar_móts_lína = models.IntegerField(db_column='Keppnisgreinar móts lína')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_dag_og_mánuð = models.SmallIntegerField(db_column='Vantar dag og mánuð')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldursflokkur_öldunga = models.CharField(db_column='Aldursflokkur öldunga', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_greinar = models.CharField(db_column='Tákn Greinar', max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldursflokkur_frí = models.CharField(db_column='Aldursflokkur FRÍ', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metaupplýsingar = models.CharField(db_column='Metaupplýsingar', max_length=50)  # Field name made lowercase.
    sama_afrek_tvisvar = models.SmallIntegerField(db_column='Sama afrek tvisvar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uppfært_á_fri_is = models.SmallIntegerField(db_column='Uppfært á FRI_IS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    replication_counter = models.IntegerField(db_column='Replication Counter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kóti_tegund_móts = models.CharField(db_column='Kóti Tegund Móts', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Afrek með öldungastigum'
        unique_together = (('úti_inni', 'kyn', 'grein', 'flokkur', 'raðsvæði', 'dagsetning', 'riðill', 'röð_innan_greinar', 'lína'), ('keppandanúmer', 'grein', 'flokkur', 'úti_inni', 'raðsvæði', 'dagsetning', 'lína'), ('heiti_móts', 'dagsetning', 'grein', 'lína'), ('mót', 'kyn', 'grein', 'flokkur', 'raðsvæði', 'röð_innan_greinar', 'lína'), ('mót', 'kyn', 'flokkur', 'lína'), ('tegund_móts', 'úti_inni', 'kyn', 'grein', 'flokkur', 'raðsvæði', 'dagsetning', 'riðill', 'röð', 'lína'), ('mót', 'grein_númer', 'raðsvæði', 'röð_innan_greinar', 'röð', 'lína'), ('aldursflokkur_öldunga', 'úti_inni', 'kyn', 'grein', 'flokkur', 'raðsvæði', 'dagsetning', 'riðill', 'röð_innan_greinar', 'lína'), ('replication_counter', 'lína'), ('félag', 'keppandanúmer', 'dagsetning', 'lína'),)


class AthlAldursflokkarFr(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    tákn = models.CharField(db_column='Tákn', primary_key=True, max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    aldur_frá = models.IntegerField(db_column='Aldur frá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_til = models.IntegerField(db_column='Aldur Til')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti = models.CharField(db_column='Heiti', max_length=30)  # Field name made lowercase.
    stutt_heiti = models.CharField(db_column='Stutt heiti', max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldursflokkur = models.SmallIntegerField(db_column='Aldursflokkur')  # Field name made lowercase.
    þágufallsheiti = models.CharField(db_column='Þágufallsheiti', max_length=30)  # Field name made lowercase.
    leitarheiti = models.CharField(db_column='Leitarheiti', max_length=30)  # Field name made lowercase.
    röð_í_afrekaskrá = models.IntegerField(db_column='Röð í afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_frá_í_afrekaskrá_field = models.IntegerField(db_column='Aldur frá (í afrekaskrá)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    aldur_til_í_afrekaskrá_field = models.IntegerField(db_column='Aldur til (í afrekaskrá)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    enskt_heiti_aldursflokks = models.CharField(db_column='Enskt heiti aldursflokks', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    flokkaafmörkun_v_afrekaskrá = models.CharField(db_column='Flokkaafmörkun v_ afrekaskrá', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lína_í_afrekaskrá_html = models.IntegerField(db_column='Lína í afrekaskrá HTML')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    viðbótarstafur_skráa_í_afr_skr = models.CharField(db_column='Viðbótarstafur skráa í afr_skr', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enskt_heiti_stutt_field = models.CharField(db_column='Enskt heiti (stutt)', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    birta_iaaf_stig = models.SmallIntegerField(db_column='Birta IAAF stig')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nota_tákn_eða_aldur_í_afr_skrá = models.IntegerField(db_column='Nota tákn eða aldur í afr_skrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skrá_íslandsmet = models.SmallIntegerField(db_column='Skrá Íslandsmet')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_í_afrekaskrá = models.CharField(db_column='Heiti í afrekaskrá', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_fyrir_kyn_og_flokk = models.CharField(db_column='Tákn fyrir kyn og flokk', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Aldursflokkar FRÍ'
        unique_together = (('leitarheiti', 'tákn'), ('kyn', 'aldur_frá', 'aldur_til', 'tákn'), ('röð_í_afrekaskrá', 'tákn'), ('lína_í_afrekaskrá_html', 'tákn'), ('kyn', 'aldur_til_í_afrekaskrá_field', 'tákn'),)


class AthlAldursflokkarldunga(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    kóti = models.CharField(db_column='Kóti', primary_key=True, max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    heiti_flokks = models.CharField(db_column='Heiti flokks', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_frá = models.IntegerField(db_column='Aldur frá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_til = models.IntegerField(db_column='Aldur til')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enskt_heiti_flokks = models.CharField(db_column='Enskt heiti flokks', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    viðbótarstafir_v_afrekaskrár = models.CharField(db_column='Viðbótarstafir v afrekaskrár', max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Aldursflokkar öldunga'
        unique_together = (('kyn', 'aldur_frá', 'aldur_til', 'kóti'), ('heiti_flokks', 'kóti'),)


class AthlAllarInnlesnarFlgurRm2013(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    flögunúmer = models.CharField(db_column='Flögunúmer', max_length=10)  # Field name made lowercase.
    tími = models.CharField(db_column='Tími', max_length=30)  # Field name made lowercase.
    skráarheiti = models.CharField(db_column='Skráarheiti', max_length=250)  # Field name made lowercase.
    rásnúmer_skv_skilgreiningu = models.IntegerField(db_column='Rásnúmer skv_ skilgreiningu')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_keppanda = models.IntegerField(db_column='Rásnúmer keppanda')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eitt_mót_úr_hlauparöðinni = models.CharField(db_column='Eitt mót úr hlauparöðinni', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Allar innlesnar flögur RM2013'
        unique_together = (('rásnúmer_skv_skilgreiningu', 'tími', 'lína'), ('flögunúmer', 'tími', 'lína'), ('tími', 'lína'),)


class AthlAllarInnlesnarFlgurHlaupga(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    flögunúmer = models.CharField(db_column='Flögunúmer', max_length=10)  # Field name made lowercase.
    tími = models.CharField(db_column='Tími', max_length=30)  # Field name made lowercase.
    skráarheiti = models.CharField(db_column='Skráarheiti', max_length=250)  # Field name made lowercase.
    rásnúmer_skv_skilgreiningu = models.IntegerField(db_column='Rásnúmer skv_ skilgreiningu')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_keppanda = models.IntegerField(db_column='Rásnúmer keppanda')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eitt_mót_úr_hlauparöðinni = models.CharField(db_column='Eitt mót úr hlauparöðinni', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Allar innlesnar flögur hlaupGA'
        unique_together = (('rásnúmer_skv_skilgreiningu', 'tími', 'lína'), ('flögunúmer', 'tími', 'lína'), ('tími', 'lína'),)


class AthlAllarInnlesnarFlgurHlaups(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    flokkur_hlaups = models.CharField(db_column='Flokkur hlaups', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    flögunúmer = models.CharField(db_column='Flögunúmer', max_length=10)  # Field name made lowercase.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    tími = models.CharField(db_column='Tími', max_length=30)  # Field name made lowercase.
    skráarheiti = models.CharField(db_column='Skráarheiti', max_length=250)  # Field name made lowercase.
    rásnúmer_skv_skilgreiningu = models.IntegerField(db_column='Rásnúmer skv_ skilgreiningu')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_keppanda = models.IntegerField(db_column='Rásnúmer keppanda')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eitt_mót_úr_hlauparöðinni = models.CharField(db_column='Eitt mót úr hlauparöðinni', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    staðsetning = models.CharField(db_column='Staðsetning', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Allar innlesnar flögur hlaups'
        unique_together = (('flokkur_hlaups', 'flögunúmer', 'lína'), ('flokkur_hlaups', 'rásnúmer_skv_skilgreiningu', 'tími', 'flögunúmer', 'lína'), ('flokkur_hlaups', 'tími', 'flögunúmer', 'lína'),)


class AthlAnnaHeitiFlags(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    félag = models.CharField(db_column='Félag', primary_key=True, max_length=10)  # Field name made lowercase.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    annað_heiti = models.CharField(db_column='Annað heiti', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Annað heiti félags'
        unique_together = (('félag', 'lína'), ('annað_heiti', 'félag', 'lína'),)


class AthlAnnaNafnKeppanda(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    keppandi_nr_field = models.CharField(db_column='Keppandi nr_', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    annað_nafn = models.CharField(db_column='Annað nafn', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Annað nafn keppanda'
        unique_together = (('keppandi_nr_field', 'lína'), ('annað_nafn', 'keppandi_nr_field', 'lína'),)


class AthlApplicationForAccessToSyst(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lineno = models.IntegerField(db_column='LineNo', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=100)  # Field name made lowercase.
    emailaddressagain = models.CharField(db_column='EmailAddressAgain', max_length=100)  # Field name made lowercase.
    club1 = models.CharField(db_column='Club1', max_length=10)  # Field name made lowercase.
    club2 = models.CharField(db_column='Club2', max_length=10)  # Field name made lowercase.
    club3 = models.CharField(db_column='Club3', max_length=10)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=30)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=50)  # Field name made lowercase.
    datetime_applied = models.DateTimeField(db_column='DateTime Applied')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Application for Access to Syst'
        unique_together = (('userid', 'lineno'),)


class AthlAthVantarMet(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    grein = models.CharField(db_column='Grein', primary_key=True, max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    aldursflokkur_frí = models.CharField(db_column='Aldursflokkur FRÍ', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fjöldi = models.IntegerField(db_column='Fjöldi')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Ath - vantar met'
        unique_together = (('grein', 'kyn', 'flokkur', 'úti_inni', 'aldursflokkur_frí'),)


class AthlAthleticslogfile(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entryno = models.IntegerField(db_column='EntryNo', primary_key=True)  # Field name made lowercase.
    dateandtime = models.DateTimeField(db_column='DateAndTime')  # Field name made lowercase.
    userinfo = models.CharField(db_column='UserInfo', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250)  # Field name made lowercase.
    competitoincode = models.CharField(db_column='CompetitoinCode', max_length=10)  # Field name made lowercase.
    competitorcode = models.CharField(db_column='CompetitorCode', max_length=10)  # Field name made lowercase.
    eventcode = models.CharField(db_column='EventCode', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$AthleticsLogFile'
        unique_together = (('dateandtime', 'entryno'), ('userinfo', 'entryno'), ('competitoincode', 'competitorcode', 'eventcode', 'entryno'), ('competitoincode', 'dateandtime', 'entryno'),)


class AthlAalflg(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$AðalFélög'


class AthlAgangsheimildir(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    user_id = models.CharField(db_column='User ID', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nafn = models.CharField(db_column='Nafn', max_length=30)  # Field name made lowercase.
    aðgangur = models.IntegerField(db_column='Aðgangur')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Aðgangsheimildir'


class AthlBackupCompetitorsinevent(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    datetimeversion = models.DateTimeField(db_column='DateTimeVersion', primary_key=True)  # Field name made lowercase.
    mot = models.CharField(max_length=10)
    greinarnumer = models.IntegerField()
    lina = models.IntegerField()
    grein = models.CharField(max_length=10)
    kyn = models.IntegerField()
    flokkur = models.CharField(max_length=10)
    ridill = models.IntegerField()
    numerridilsekkinotad = models.IntegerField()
    dagsetninggreinar = models.DateTimeField()
    timigreinar = models.DateTimeField()
    rasnumer = models.IntegerField()
    leitarnafn = models.CharField(max_length=30)
    ridillnumer = models.IntegerField()
    stokkkastrod = models.IntegerField()
    nafn = models.CharField(max_length=35)
    faedingarar = models.IntegerField()
    felag = models.CharField(max_length=10)
    timi = models.DecimalField(max_digits=38, decimal_places=20)
    metrar = models.DecimalField(max_digits=38, decimal_places=20)
    vindur = models.DecimalField(max_digits=38, decimal_places=20)
    arangur = models.CharField(max_length=10)
    rafmagnstimataka = models.SmallIntegerField()
    thrautarstig = models.IntegerField()
    urslitarod = models.IntegerField()
    samasaetiognaestiaundan = models.SmallIntegerField()
    nanarirod = models.IntegerField()
    stig = models.DecimalField(max_digits=38, decimal_places=20)
    stadakeppni = models.IntegerField()
    urslitarodtexti = models.CharField(max_length=10)
    iaaf_stig = models.IntegerField(db_column='IAAF Stig')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tilraun1 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur1 = models.DecimalField(max_digits=38, decimal_places=20)
    merking1 = models.IntegerField()
    tilraun2 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur2 = models.DecimalField(max_digits=38, decimal_places=20)
    merking2 = models.IntegerField()
    tilraun3 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur3 = models.DecimalField(max_digits=38, decimal_places=20)
    merking3 = models.IntegerField()
    tilraun4 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur4 = models.DecimalField(max_digits=38, decimal_places=20)
    merking4 = models.IntegerField()
    tilraun5 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur5 = models.DecimalField(max_digits=38, decimal_places=20)
    merking5 = models.IntegerField()
    tilraun6 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur6 = models.DecimalField(max_digits=38, decimal_places=20)
    merking6 = models.IntegerField()
    sortorder1 = models.DecimalField(max_digits=38, decimal_places=20)
    sortorder2 = models.DecimalField(max_digits=38, decimal_places=20)
    seria = models.CharField(max_length=100)
    athugasemd = models.CharField(max_length=20)
    handvirkathugasemd = models.SmallIntegerField()
    nullarangur = models.SmallIntegerField()
    bestiaranguriar = models.DecimalField(max_digits=38, decimal_places=20)
    personulegmet = models.DecimalField(max_digits=38, decimal_places=20)
    bestiaranguriartexti = models.CharField(max_length=15)
    personulegtmettexti = models.CharField(max_length=15)
    rodiundanurslitum = models.IntegerField()
    qualification = models.CharField(max_length=1)
    gestur = models.SmallIntegerField()
    handvirkstig = models.SmallIntegerField()
    rasnumeraskyrslu = models.IntegerField()
    unglingastig = models.IntegerField(db_column='Unglingastig')  # Field name made lowercase.
    performaceremarks = models.CharField(db_column='PerformaceRemarks', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$BACKUP CompetitorsInEvent'
        unique_together = (('datetimeversion', 'mot', 'greinarnumer', 'lina'), ('mot', 'grein', 'kyn', 'flokkur', 'datetimeversion', 'greinarnumer', 'lina'),)


class AthlBatchPostingLoadSchedule(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    from_time = models.DateTimeField(db_column='From Time', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    to_time = models.DateTimeField(db_column='To Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wait_between_tasks_sec_field = models.IntegerField(db_column='Wait between Tasks (sec)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    max_no_of_lines = models.IntegerField(db_column='Max No_ of Lines')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Batch Posting Load Schedule'
        unique_together = (('to_time', 'from_time'),)


class AthlBestuAfrekRmMAldursfl(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    raðsvæði = models.DecimalField(db_column='Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=10)  # Field name made lowercase.
    vindur = models.DecimalField(db_column='Vindur', max_digits=38, decimal_places=20)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    metrar = models.DecimalField(db_column='Metrar', max_digits=38, decimal_places=20)  # Field name made lowercase.
    tími = models.CharField(db_column='Tími', max_length=10)  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    löglegt = models.SmallIntegerField(db_column='Löglegt')  # Field name made lowercase.
    röð = models.CharField(db_column='Röð', max_length=10)  # Field name made lowercase.
    rafmagnstímataka = models.SmallIntegerField(db_column='Rafmagnstímataka')  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    aldur_keppanda = models.IntegerField(db_column='Aldur keppanda')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mót = models.CharField(db_column='Mót', max_length=10)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    heiti_móts = models.CharField(db_column='Heiti Móts', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sería = models.CharField(db_column='Sería', max_length=100)  # Field name made lowercase.
    aldursflokkur_í_hlaupi = models.CharField(db_column='Aldursflokkur í hlaupi', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_í_afrekaskrá_ársins = models.IntegerField(db_column='Röð í afrekaskrá ársins')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_í_afrekaskrá_flokksins = models.IntegerField(db_column='Röð í afrekaskrá flokksins')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    riðill = models.IntegerField(db_column='Riðill')  # Field name made lowercase.
    félag_innan_sambands = models.CharField(db_column='Félag innan sambands', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_vind = models.SmallIntegerField(db_column='Vantar vind')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    erlendur_ríkisborgari = models.SmallIntegerField(db_column='Erlendur ríkisborgari')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ekki_í_afrekaskrá = models.SmallIntegerField(db_column='Ekki í afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tegund_móts = models.IntegerField(db_column='Tegund móts')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grein_númer = models.IntegerField(db_column='Grein númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_innan_greinar = models.IntegerField(db_column='Röð innan greinar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keppnisgreinar_móts_lína = models.IntegerField(db_column='Keppnisgreinar móts lína')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_dag_og_mánuð = models.SmallIntegerField(db_column='Vantar dag og mánuð')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sama_afrek_tvisvar = models.SmallIntegerField(db_column='Sama afrek tvisvar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uppfært_á_fri_is = models.SmallIntegerField(db_column='Uppfært á FRI_IS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_í_hlaupi = models.IntegerField(db_column='Röð í hlaupi')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_í_flokki = models.IntegerField(db_column='Röð í flokki')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Bestu afrek í RM m aldursfl'
        unique_together = (('grein', 'kyn', 'aldursflokkur_í_hlaupi', 'raðsvæði', 'dagsetning', 'röð_í_flokki', 'lína'), ('grein', 'aldursflokkur_í_hlaupi', 'keppandanúmer', 'lína'), ('grein', 'kyn', 'raðsvæði', 'dagsetning', 'röð_í_hlaupi', 'lína'), ('keppandanúmer', 'lína'),)


class AthlBrautarskiptStkkKastr(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót = models.CharField(db_column='Mót', primary_key=True, max_length=10)  # Field name made lowercase.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    a = models.IntegerField(db_column='A')  # Field name made lowercase.
    b = models.IntegerField(db_column='B')  # Field name made lowercase.
    c = models.IntegerField(db_column='C')  # Field name made lowercase.
    d = models.IntegerField(db_column='D')  # Field name made lowercase.
    e = models.IntegerField(db_column='E')  # Field name made lowercase.
    f = models.IntegerField(db_column='F')  # Field name made lowercase.
    g = models.IntegerField(db_column='G')  # Field name made lowercase.
    h = models.IntegerField(db_column='H')  # Field name made lowercase.
    i = models.IntegerField(db_column='I')  # Field name made lowercase.
    j = models.IntegerField(db_column='J')  # Field name made lowercase.
    k = models.IntegerField(db_column='K')  # Field name made lowercase.
    l = models.IntegerField(db_column='L')  # Field name made lowercase.
    m = models.IntegerField(db_column='M')  # Field name made lowercase.
    n = models.IntegerField(db_column='N')  # Field name made lowercase.
    o = models.IntegerField(db_column='O')  # Field name made lowercase.
    p = models.IntegerField(db_column='P')  # Field name made lowercase.
    q = models.IntegerField(db_column='Q')  # Field name made lowercase.
    r = models.IntegerField(db_column='R')  # Field name made lowercase.
    s = models.IntegerField(db_column='S')  # Field name made lowercase.
    t = models.IntegerField(db_column='T')  # Field name made lowercase.
    innsta_braut = models.IntegerField(db_column='Innsta braut')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Brautarskipt, stökk-, kaströð'
        unique_together = (('mót', 'lína'), ('mót', 'kyn', 'grein', 'lína'),)


class AthlBufferFyrirIaafScoringtabls(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    reitur1 = models.CharField(db_column='Reitur1', max_length=30)  # Field name made lowercase.
    reitur2 = models.CharField(db_column='Reitur2', max_length=30)  # Field name made lowercase.
    reitur3 = models.CharField(db_column='Reitur3', max_length=30)  # Field name made lowercase.
    reitur4 = models.CharField(db_column='Reitur4', max_length=30)  # Field name made lowercase.
    reitur5 = models.CharField(db_column='Reitur5', max_length=30)  # Field name made lowercase.
    reitur6 = models.CharField(db_column='Reitur6', max_length=30)  # Field name made lowercase.
    reitur7 = models.CharField(db_column='Reitur7', max_length=30)  # Field name made lowercase.
    reitur8 = models.CharField(db_column='Reitur8', max_length=30)  # Field name made lowercase.
    reitur9 = models.CharField(db_column='Reitur9', max_length=30)  # Field name made lowercase.
    reitur10 = models.CharField(db_column='Reitur10', max_length=30)  # Field name made lowercase.
    reitur11 = models.CharField(db_column='Reitur11', max_length=30)  # Field name made lowercase.
    reitur12 = models.CharField(db_column='Reitur12', max_length=30)  # Field name made lowercase.
    reitur13 = models.CharField(db_column='Reitur13', max_length=30)  # Field name made lowercase.
    reitur14 = models.CharField(db_column='Reitur14', max_length=30)  # Field name made lowercase.
    reitur15 = models.CharField(db_column='Reitur15', max_length=30)  # Field name made lowercase.
    points_er_í_dálki = models.IntegerField(db_column='Points er í dálki')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    ár = models.IntegerField(db_column='Ár')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Buffer fyrir IAAF ScoringTabls'


class AthlBtingarMillira(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    tákn_keyrslu = models.CharField(db_column='Tákn keyrslu', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=50)  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    aldur_í_ár = models.IntegerField(db_column='Aldur í ár')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    heiti_greinar = models.CharField(db_column='Heiti greinar', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    árangur_í_fyrra = models.CharField(db_column='Árangur í fyrra', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    árangur_í_ár = models.CharField(db_column='Árangur í ár', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bæting_í_sekúndum = models.DecimalField(db_column='Bæting í sekúndum', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bæting_í_metrum = models.DecimalField(db_column='Bæting í metrum', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_í_afrekaksrá = models.DecimalField(db_column='Röð í afrekaksrá', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    viðmiðunarár = models.IntegerField(db_column='Viðmiðunarár')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Bætingar á milli ára'
        unique_together = (('tákn_keyrslu', 'lína'), ('tákn_keyrslu', 'félag', 'keppandanúmer', 'röð_í_afrekaksrá', 'lína'),)


class AthlCharityOrganizations(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    flokkur_hlaups = models.CharField(db_column='Flokkur hlaups', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    charity_id_no_field = models.IntegerField(db_column='Charity ID No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    charity_name = models.CharField(db_column='Charity Name', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    charity_social_sec_no_field = models.CharField(db_column='Charity Social Sec_ No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    english_name_of_charity = models.CharField(db_column='English Name of Charity', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Charity Organizations'
        unique_together = (('flokkur_hlaups', 'charity_id_no_field'),)


class AthlClubs(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    félag = models.CharField(db_column='Félag', primary_key=True, max_length=10)  # Field name made lowercase.
    stutt_heiti = models.CharField(db_column='Stutt heiti', max_length=17)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_félags = models.CharField(db_column='Heiti félags', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heimili = models.CharField(db_column='Heimili', max_length=30)  # Field name made lowercase.
    póstfang = models.CharField(db_column='Póstfang', max_length=30)  # Field name made lowercase.
    merki = models.BinaryField(db_column='Merki', blank=True, null=True)  # Field name made lowercase.
    fjöldi_brauta_á_félagsvelli = models.IntegerField(db_column='Fjöldi brauta á félagsvelli')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þágufall = models.CharField(db_column='Þágufall', max_length=30)  # Field name made lowercase.
    framkvæmdastjóri = models.CharField(db_column='Framkvæmdastjóri', max_length=30)  # Field name made lowercase.
    bt_field = models.CharField(db_column='Bt_', max_length=30)  # Field name made lowercase. Field renamed because it ended with '_'.
    heimili_framkv_stjóra = models.CharField(db_column='Heimili Framkv_stjóra', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    póstfang_framkv_stjóra = models.CharField(db_column='Póstfang Framkv_stjóra', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tegund = models.IntegerField(db_column='Tegund')  # Field name made lowercase.
    héraðssamband = models.CharField(db_column='Héraðssamband', max_length=10)  # Field name made lowercase.
    númer_félags_kappi_field = models.IntegerField(db_column='Númer félags (Kappi)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    leitarheiti = models.CharField(db_column='Leitarheiti', max_length=30)  # Field name made lowercase.
    heiti_html_síðu = models.CharField(db_column='Heiti HTML síðu', max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mynda_html_afrekaskrá = models.SmallIntegerField(db_column='Mynda HTML afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eignarfall = models.CharField(db_column='Eignarfall', max_length=30)  # Field name made lowercase.
    heimasíða = models.CharField(db_column='Heimasíða', max_length=50)  # Field name made lowercase.
    enskt_heiti = models.CharField(db_column='Enskt heiti', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sameiginlegt_félag = models.SmallIntegerField(db_column='Sameiginlegt félag')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Clubs'
        unique_together = (('héraðssamband', 'félag'), ('leitarheiti', 'félag'), ('tegund', 'félag'), ('heiti_html_síðu', 'félag'), ('heiti_félags', 'félag'),)


class AthlClubsincompetition(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mot = models.CharField(primary_key=True, max_length=10)
    lina = models.IntegerField()
    felag = models.CharField(max_length=10)
    bokstafur = models.CharField(max_length=10)
    kyn = models.IntegerField()
    reiknudstig = models.DecimalField(max_digits=38, decimal_places=20)
    fjoldisigra = models.DecimalField(max_digits=38, decimal_places=20)
    radsvaedi3 = models.DecimalField(max_digits=38, decimal_places=20)
    utreiknudrod = models.CharField(max_length=10)
    gestalid = models.SmallIntegerField()
    wrkstig1 = models.DecimalField(max_digits=38, decimal_places=20)
    wrkstig2 = models.DecimalField(max_digits=38, decimal_places=20)
    wrkstig3 = models.DecimalField(max_digits=38, decimal_places=20)
    fyrstihluti = models.DecimalField(max_digits=38, decimal_places=20)

    class Meta:
        managed = False
        db_table = 'Athl$ClubsInCompetition'
        unique_together = (('mot', 'lina'), ('mot', 'bokstafur', 'lina'), ('mot', 'reiknudstig', 'fjoldisigra', 'radsvaedi3', 'lina'), ('mot', 'felag', 'kyn', 'lina'),)


class AthlCommentLine(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    table_name = models.IntegerField(db_column='Table Name', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    no_field = models.CharField(db_column='No_', max_length=20)  # Field name made lowercase. Field renamed because it ended with '_'.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=10)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Comment Line'
        unique_together = (('table_name', 'no_field', 'line_no_field'),)


class AthlCompare2Obj(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    pos_1 = models.IntegerField(db_column='POS 1', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pos_2 = models.IntegerField(db_column='POS 2')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    i1 = models.DecimalField(db_column='I1', max_digits=38, decimal_places=20)  # Field name made lowercase.
    i2 = models.DecimalField(db_column='I2', max_digits=38, decimal_places=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Compare 2 obj'


class AthlCompetition(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    code = models.CharField(db_column='Code', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=30)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    date2 = models.DateTimeField(db_column='Date2')  # Field name made lowercase.
    date3 = models.DateTimeField(db_column='Date3')  # Field name made lowercase.
    organizer = models.CharField(db_column='Organizer', max_length=30)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=30)  # Field name made lowercase.
    judge = models.CharField(db_column='Judge', max_length=30)  # Field name made lowercase.
    outdoorsorindoors = models.IntegerField(db_column='OutdoorsOrIndoors')  # Field name made lowercase.
    competitontype = models.IntegerField(db_column='CompetitonType')  # Field name made lowercase.
    fjolditilstiga = models.IntegerField()
    stigfyrir1saeti = models.IntegerField()
    stigfyrir2saeti = models.IntegerField()
    allirfastig = models.SmallIntegerField()
    tegundstigakeppni = models.IntegerField()
    fjoldibrauta = models.IntegerField()
    skraningargjaldprgrein = models.DecimalField(max_digits=38, decimal_places=20)
    undirskriftgjaldkera = models.CharField(max_length=30)
    rafmagnstimataka = models.SmallIntegerField()
    heitiiafrekaskra = models.CharField(max_length=50)
    fjoldiumferdaitaeknigreinum = models.IntegerField()
    staðurgreinainnanbæjarfélags = models.SmallIntegerField()
    dagsetning4 = models.DateTimeField()
    tími = models.DateTimeField(db_column='Tími')  # Field name made lowercase.
    skráningargjld_f_boðhlaup = models.DecimalField(db_column='Skráningargjld f_ boðhlaup', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skráningargj_yngri_en_18_ára = models.DecimalField(db_column='Skráningargj_ yngri en 18 ára', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skráningargj_f_boðhl_y_18_ára = models.DecimalField(db_column='Skráningargj_ f boðhl y 18 ára', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantardagogmanud = models.SmallIntegerField()
    lengdikm = models.DecimalField(max_digits=38, decimal_places=20)
    systurhlaup1 = models.CharField(max_length=10)
    systurhlaup2 = models.CharField(max_length=10)
    systurhlaup3 = models.CharField(max_length=10)
    hlaupmotifyrra = models.CharField(max_length=10)
    vidbotvtimatoku1 = models.IntegerField()
    greiniafrekaskra = models.CharField(max_length=10)
    bokadiafrekaskra = models.SmallIntegerField()
    vidbotvtimatoku = models.CharField(max_length=10)
    endanlegurslitskrad = models.SmallIntegerField()
    raesitimi = models.DateTimeField()
    synaathugasemd = models.SmallIntegerField()
    oldungaflokkar = models.SmallIntegerField()
    tungumal = models.IntegerField()
    synafelag = models.SmallIntegerField()
    synaheitisveitar = models.SmallIntegerField()
    taknhlaupsvidinnlestur = models.CharField(max_length=50)
    ensktheitiamoti = models.CharField(max_length=50)
    heitihtmlsidu = models.CharField(max_length=15)
    aldursflokkamot = models.SmallIntegerField()
    makeppauppfyrirsig = models.SmallIntegerField()
    ritarablodmedislmeti = models.SmallIntegerField()
    synaland = models.SmallIntegerField()
    athugasemdaurslitabladi = models.CharField(max_length=150)
    reikna_unglingastig = models.SmallIntegerField(db_column='Reikna unglingastig')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dagssídastuppfaert = models.DateTimeField()
    timisídastuppfaert = models.DateTimeField()
    bodhlaupmedmismsprettum = models.SmallIntegerField()
    textividgesti = models.CharField(max_length=10)
    synanettotima = models.SmallIntegerField()
    greiniafrekaskraflogutimi = models.CharField(max_length=10)
    notafelagafkeppendaspjaldi = models.SmallIntegerField()
    lokamotivafrekaskrar = models.SmallIntegerField()
    landistadfelags = models.SmallIntegerField()
    ekkibirtaiafrekaskra = models.SmallIntegerField()
    slodaurslitmots = models.CharField(max_length=50)
    synamillitima1 = models.SmallIntegerField()
    synamillitima2 = models.SmallIntegerField()
    heitialista = models.CharField(max_length=60)
    keppnisvollur = models.CharField(max_length=50)
    floguhlaup = models.SmallIntegerField()
    nanaritegund = models.IntegerField()
    hlaupaseria = models.CharField(max_length=10)
    flokkurhlaups = models.CharField(max_length=10)
    tegundmots = models.CharField(max_length=10)
    synamillitima3 = models.SmallIntegerField()
    teljarialltaf1 = models.DecimalField(max_digits=38, decimal_places=20)
    stofna_nýjan_v_innles_á_millit = models.SmallIntegerField(db_column='Stofna nýjan v innles á millit')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    millitímar_teknir_eftir = models.CharField(db_column='Millitímar teknir eftir', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nota_aðeins_ársbesta_við_röðun = models.SmallIntegerField(db_column='Nota aðeins ársbesta við röðun')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tímabil_ársbesta_frá_mótsdags = models.CharField(db_column='Tímabil ársbesta frá mótsdags', max_length=32)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reikna_iaaf_stig = models.SmallIntegerField(db_column='Reikna IAAF stig')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    má_prenta_úrslit_frá_scheduler = models.SmallIntegerField(db_column='Má prenta úrslit frá Scheduler')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    synamillitima4 = models.SmallIntegerField()
    synamillitima5 = models.SmallIntegerField()
    með_rásnúmeri = models.SmallIntegerField(db_column='Með rásnúmeri')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleppa_í_afhendingu_rásnúmera = models.SmallIntegerField(db_column='Sleppa í afhendingu rásnúmera')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    competitorsminimumage = models.IntegerField(db_column='CompetitorsMinimumAge')  # Field name made lowercase.
    staða_móts = models.IntegerField(db_column='Staða móts')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    entryfeetype = models.IntegerField(db_column='EntryFeeType')  # Field name made lowercase.
    entryfeeprclub = models.DecimalField(db_column='EntryFeePrClub', max_digits=38, decimal_places=20)  # Field name made lowercase.
    maxageforfee1 = models.IntegerField(db_column='MaxAgeForFee1')  # Field name made lowercase.
    entryfeeprcompetitor1 = models.DecimalField(db_column='EntryFeePrCompetitor1', max_digits=38, decimal_places=20)  # Field name made lowercase.
    maxageforfee2 = models.IntegerField(db_column='MaxAgeForFee2')  # Field name made lowercase.
    entryfeeprcompetitor2 = models.DecimalField(db_column='EntryFeePrCompetitor2', max_digits=38, decimal_places=20)  # Field name made lowercase.
    maxageforfee3 = models.IntegerField(db_column='MaxAgeForFee3')  # Field name made lowercase.
    entryfeeprcompetitor3 = models.DecimalField(db_column='EntryFeePrCompetitor3', max_digits=38, decimal_places=20)  # Field name made lowercase.
    maximumentryfeeprcompetitor = models.DecimalField(db_column='MaximumEntryFeePrCompetitor', max_digits=38, decimal_places=20)  # Field name made lowercase.
    defaulttaborderonentryforms = models.IntegerField(db_column='DefaultTabOrderOnEntryForms')  # Field name made lowercase.
    displaycolumnforprizeceremony = models.SmallIntegerField(db_column='DisplayColumnForPrizeCeremony')  # Field name made lowercase.
    competitionfinalized = models.SmallIntegerField(db_column='CompetitionFinalized')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Competition'
        unique_together = (('competitontype', 'code'), ('date', 'tími', 'code'), ('name', 'date', 'code'), ('heitihtmlsidu', 'code'), ('taknhlaupsvidinnlestur', 'code'), ('date', 'competitontype', 'outdoorsorindoors', 'code'), ('flokkurhlaups', 'code'), ('tegundmots', 'code'),)


class AthlCompetitionevents(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mot = models.CharField(primary_key=True, max_length=10)
    lina = models.IntegerField()
    grein = models.CharField(max_length=10)
    kyn = models.IntegerField()
    flokkur = models.CharField(max_length=10)
    ridill = models.IntegerField()
    numerridils = models.IntegerField()
    dagsetning = models.DateTimeField()
    timi = models.DateTimeField()
    stadur = models.CharField(max_length=30)
    nafnakall = models.DateTimeField()
    timi2ridils = models.DateTimeField()
    heitigreinar = models.CharField(max_length=80)
    ensktheitigreinar = models.CharField(max_length=80)
    tegundgreinar = models.IntegerField()
    rafmagnstimataka = models.SmallIntegerField()
    krefstvindmaelis = models.SmallIntegerField()
    nanaritegundargreining = models.IntegerField()
    thrautargrein = models.SmallIntegerField()
    sería_með_stigum_í_þrautargr_field = models.SmallIntegerField(db_column='Sería með stigum í þrautargr_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fjoldiibrauta = models.IntegerField()
    fjoldiumferda = models.IntegerField()
    aldurfra = models.IntegerField()
    aldurtil = models.IntegerField()
    stigagrein = models.SmallIntegerField()
    fjolditilstiga = models.IntegerField()
    stigfyrir1saeti = models.IntegerField()
    stigfyrir2saeti = models.IntegerField()
    handvirkstigaskraning = models.SmallIntegerField()
    teljagreinistigautreikningi = models.SmallIntegerField()
    röð_kepp_sem_fær_fyrst_stig = models.IntegerField(db_column='Röð kepp_ sem fær fyrst stig')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skraningargjald = models.DecimalField(max_digits=38, decimal_places=20)
    urslitkomin = models.SmallIntegerField()
    birtaiurslitum = models.SmallIntegerField()
    stadakeppni = models.IntegerField()
    takngreinar = models.CharField(max_length=20)
    rodiurslitum = models.IntegerField()
    urridliaundankoma = models.IntegerField()
    hamarkfjoldikeppenda = models.IntegerField()
    sigurvegariifyrra = models.CharField(max_length=100)
    arangurifyrra = models.CharField(max_length=10)
    motsmetshafi = models.CharField(max_length=100)
    motsmet = models.CharField(max_length=15)
    dagsetningmotsmets = models.DateTimeField()
    stadurmotsmets = models.CharField(max_length=20)
    felagmotsmetshafa = models.CharField(max_length=10)
    rodiafrekaskra = models.IntegerField()
    rodithraut = models.IntegerField()
    motsmetshafi2 = models.CharField(max_length=100)
    motsmet2 = models.CharField(max_length=10)
    dagsetningmotsmets2 = models.DateTimeField()
    stadurmotsmets2 = models.CharField(max_length=20)
    felagmotsmetshafa2 = models.CharField(max_length=10)
    tharfadradakeppendum = models.SmallIntegerField()
    athugasemd = models.CharField(max_length=50)
    athugasemdaritarablad = models.CharField(max_length=50)
    heitihtmlskrar = models.CharField(max_length=50)
    htmlskramyndudthann = models.DateTimeField()
    htmlskramyndudkl = models.DateTimeField()
    eventnamefisi = models.CharField(max_length=30)
    númer_hlaupagreinar_f_lynx = models.IntegerField(db_column='Númer hlaupagreinar f_ Lynx')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tilkynnaurslit = models.IntegerField()
    tilkynnaverdlaunaafhendingu = models.IntegerField()
    ekkiprentaritarablod = models.SmallIntegerField()
    motsmetshafi3 = models.CharField(max_length=100)
    motsmet3 = models.CharField(max_length=10)
    dagsetningmotsmets3 = models.DateTimeField()
    stadurmotsmets3 = models.CharField(max_length=20)
    felagmotsmetshafa3 = models.CharField(max_length=10)
    innlesið_heiti_greinar = models.CharField(db_column='Innlesið heiti greinar', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    val_fyrir_ledstudio = models.IntegerField(db_column='Val_fyrir_LedStudio')  # Field name made lowercase.
    valfyrirsjonvarp = models.IntegerField(db_column='ValFyrirSjonvarp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$CompetitionEvents'
        unique_together = (('mot', 'lina'), ('mot', 'dagsetning', 'timi', 'lina'), ('mot', 'grein', 'kyn', 'flokkur', 'ridill', 'numerridils', 'lina'), ('mot', 'nanaritegundargreining', 'kyn', 'lina'), ('mot', 'kyn', 'rodiafrekaskra', 'lina'), ('mot', 'kyn', 'rodithraut', 'lina'), ('mot', 'birtaiurslitum', 'rodiurslitum', 'lina'), ('mot', 'dagsetning', 'grein', 'timi', 'lina'),)


class AthlCompetitionfeepayment(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entryno = models.IntegerField(db_column='EntryNo', primary_key=True)  # Field name made lowercase.
    competitioncode = models.CharField(db_column='CompetitionCode', max_length=10)  # Field name made lowercase.
    club = models.CharField(db_column='Club', max_length=10)  # Field name made lowercase.
    bibno = models.IntegerField(db_column='BibNo')  # Field name made lowercase.
    calculatedfee = models.DecimalField(db_column='CalculatedFee', max_digits=38, decimal_places=20)  # Field name made lowercase.
    paidfee = models.DecimalField(db_column='PaidFee', max_digits=38, decimal_places=20)  # Field name made lowercase.
    paymentdate = models.DateTimeField(db_column='PaymentDate')  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$CompetitionFeePayment'
        unique_together = (('entryno', 'competitioncode', 'club', 'bibno'),)


class AthlCompetitionfees(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    competitioncode = models.CharField(db_column='CompetitionCode', primary_key=True, max_length=10)  # Field name made lowercase.
    club = models.CharField(db_column='Club', max_length=10)  # Field name made lowercase.
    bibno = models.IntegerField(db_column='BibNo')  # Field name made lowercase.
    calculatedfee = models.DecimalField(db_column='CalculatedFee', max_digits=38, decimal_places=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$CompetitionFees'
        unique_together = (('competitioncode', 'club', 'bibno'),)


class AthlCompetitionsecretaries(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    competitioncode = models.CharField(db_column='CompetitionCode', primary_key=True, max_length=10)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$CompetitionSecretaries'


class AthlCompetitionupdateaccess(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    competitioncode = models.CharField(db_column='CompetitionCode', primary_key=True, max_length=10)  # Field name made lowercase.
    line = models.IntegerField(db_column='Line')  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100)  # Field name made lowercase.
    accesslevel = models.IntegerField(db_column='AccessLevel')  # Field name made lowercase.
    competitioncreator = models.SmallIntegerField(db_column='CompetitionCreator')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$CompetitionUpdateAccess'
        unique_together = (('competitioncode', 'line'), ('competitioncode', 'userid', 'line'),)


class AthlCompetitors(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    númer = models.CharField(db_column='Númer', primary_key=True, max_length=20)  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    heimili = models.CharField(db_column='Heimili', max_length=80)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=50)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    land = models.CharField(db_column='Land', max_length=10)  # Field name made lowercase.
    fjölskyldunúmer = models.CharField(db_column='Fjölskyldunúmer', max_length=11)  # Field name made lowercase.
    heimasími = models.CharField(db_column='Heimasími', max_length=30)  # Field name made lowercase.
    vinnusími = models.CharField(db_column='Vinnusími', max_length=30)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E-Mail', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heimili_2 = models.CharField(db_column='Heimili 2', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    merking = models.CharField(db_column='Merking', max_length=30)  # Field name made lowercase.
    félag_innan_sambands = models.CharField(db_column='Félag innan sambands', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    héraðssamband = models.CharField(db_column='Héraðssamband', max_length=10)  # Field name made lowercase.
    leitarnafn = models.CharField(db_column='Leitarnafn', max_length=35)  # Field name made lowercase.
    fæðingardagur = models.DateTimeField(db_column='Fæðingardagur')  # Field name made lowercase.
    þjóðerni = models.CharField(db_column='Þjóðerni', max_length=10)  # Field name made lowercase.
    mynd = models.BinaryField(db_column='Mynd', blank=True, null=True)  # Field name made lowercase.
    heimasíða = models.CharField(db_column='Heimasíða', max_length=50)  # Field name made lowercase.
    númer_flögu = models.CharField(db_column='Númer flögu', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    auðkenni_idega = models.CharField(db_column='Auðkenni Idega', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    með_sömu_kennitölu = models.SmallIntegerField(db_column='Með Sömu Kennitölu')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    #dags_síðast_uppfært = models.DateTimeField(db_column='Dags síðast uppfært')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    #tími_síðast_uppfært = models.DateTimeField(db_column='Tími síðast uppfært')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    annað_nafn = models.CharField(db_column='Annað nafn', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    #sleppa_í_afrekaskrá = models.SmallIntegerField(db_column='Sleppa í afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Competitors'
        unique_together = (('nafn', 'fæðingarár', 'félag', 'númer'), ('kennitala', 'með_sömu_kennitölu', 'númer'), ('félag', 'kyn', 'nafn', 'númer'), ('staður', 'heimili', 'fæðingarár', 'númer'), ('annað_nafn', 'númer'),)


class AthlCompetitorsincompetition(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mot = models.CharField(primary_key=True, max_length=10)
    rasnumer = models.IntegerField()
    keppendanumer = models.CharField(max_length=10)
    nafn = models.CharField(max_length=35)
    felag = models.CharField(max_length=10)
    felaginnansambands = models.CharField(max_length=10)
    kyn = models.IntegerField()
    kennitala = models.CharField(max_length=11)
    faedingardagur = models.DateTimeField()
    faedingarar = models.IntegerField()
    aldurkeppanda = models.IntegerField()
    aldursflokkur = models.IntegerField()
    leitarnafn = models.CharField(max_length=35)
    land = models.CharField(max_length=10)
    keppnisflokkurihlaupi = models.CharField(max_length=11)
    timinumeriskur = models.DecimalField(max_digits=38, decimal_places=20)
    timi = models.CharField(max_length=12)
    rodimark = models.IntegerField()
    rodiflokki = models.IntegerField()
    heitisveitar = models.CharField(max_length=50)
    ogreittthatttokugjald = models.SmallIntegerField()
    skraning = models.IntegerField()
    vegalengd = models.CharField(max_length=10)
    keppnisflokkur = models.IntegerField()
    skogerd = models.IntegerField()
    staerdtbols = models.IntegerField()
    athugasemd = models.CharField(max_length=50)
    numerflogu = models.CharField(max_length=10)
    starttimiklst = models.CharField(max_length=15)
    lokatimiklst = models.CharField(max_length=15)
    nettotimi = models.CharField(max_length=15)
    kaupaedaleigjaflogu = models.IntegerField()
    bruttotimi = models.CharField(max_length=15)
    bodhlaupssveit = models.SmallIntegerField()
    fyrirlidi = models.SmallIntegerField()
    millitimi1klst = models.CharField(max_length=15)
    millitimi1brutto = models.CharField(max_length=15)
    millitimi1netto = models.CharField(max_length=15)
    millitimi2klst = models.CharField(max_length=15)
    millitimi2brutto = models.CharField(max_length=15)
    millitimi2netto = models.CharField(max_length=15)
    byssutimihlaupara = models.CharField(max_length=30)
    millitimi3klst = models.CharField(max_length=15)
    millitimi3brutto = models.CharField(max_length=15)
    millitimi3netto = models.CharField(max_length=15)
    fradrvmargrarashopa = models.IntegerField()
    millitimi4klst = models.CharField(max_length=15)
    millitimi4brutto = models.CharField(max_length=15)
    millitimi4netto = models.CharField(max_length=15)
    millitimi5klst = models.CharField(max_length=15)
    millitimi5brutto = models.CharField(max_length=15)
    millitimi5netto = models.CharField(max_length=15)
    millitimi6klst = models.CharField(max_length=15)
    millitimi6brutto = models.CharField(max_length=15)
    millitimi6netto = models.CharField(max_length=15)
    linunumerfloguskrar = models.IntegerField(db_column='LinunumerFloguskrar')  # Field name made lowercase.
    rasnumeraskyrslu = models.IntegerField()
    wrkheimili = models.CharField(max_length=100)
    wrkstadur = models.CharField(max_length=100)
    vantarbol = models.SmallIntegerField()
    gestur = models.SmallIntegerField()
    skraningardags = models.DateTimeField()
    skraningartimi = models.DateTimeField()
    skradaf = models.CharField(max_length=10)
    wrkemail = models.CharField(max_length=50)
    flokkurhlaups = models.CharField(max_length=10)
    staerdbolstexti = models.CharField(db_column='StaerdBolsTexti', max_length=30)  # Field name made lowercase.
    með_medalíu = models.SmallIntegerField(db_column='Með medalíu')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    numergodgerdafelags = models.IntegerField()
    numervaraflogu = models.CharField(max_length=10)
    wrkheimilifangland = models.CharField(max_length=30)
    idegauserid = models.CharField(max_length=10)
    má_senda_e_mail = models.SmallIntegerField(db_column='Má senda e-mail')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    netskráning = models.SmallIntegerField(db_column='Netskráning')  # Field name made lowercase.
    fyrirtæki = models.CharField(db_column='Fyrirtæki', max_length=50)  # Field name made lowercase.
    í_hjólastól = models.SmallIntegerField(db_column='Í hjólastól')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    innlesið_nafn = models.CharField(db_column='Innlesið nafn', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    innlesið_fæðingarár = models.IntegerField(db_column='Innlesið fæðingarár')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    innlesið_félag = models.CharField(db_column='Innlesið félag', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    greinnumer = models.IntegerField()
    rodinnangreinar = models.IntegerField()
    úthlutað_rásnúmer = models.IntegerField(db_column='Úthlutað rásnúmer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skráningardags_rásnúmers = models.DateTimeField(db_column='Skráningardags_ rásnúmers')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skráningartími_rásnúmers = models.DateTimeField(db_column='Skráningartími rásnúmers')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skráð_í_vél = models.CharField(db_column='Skráð í vél', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skipta_yfir_í_vegalengd = models.CharField(db_column='Skipta yfir í vegalengd', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wrksimi = models.CharField(db_column='wrkSimi', max_length=50)  # Field name made lowercase.
    wrkfarsimi = models.CharField(db_column='wrkFarsimi', max_length=50)  # Field name made lowercase.
    wrkþjóðerni = models.CharField(db_column='wrkÞjóðerni', max_length=30)  # Field name made lowercase.
    announcer_remarks = models.CharField(db_column='Announcer Remarks', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    finish_line_description = models.CharField(db_column='Finish Line Description', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hlaupahópur = models.CharField(db_column='Hlaupahópur', max_length=80)  # Field name made lowercase.
    má_senda_úrslit_á_facebook = models.SmallIntegerField(db_column='Má senda úrslit á Facebook')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$CompetitorsInCompetition'
        unique_together = (('mot', 'rasnumer'), ('keppendanumer', 'mot', 'rasnumer'), ('mot', 'kyn', 'keppnisflokkurihlaupi', 'rasnumer'), ('mot', 'felag', 'rodimark', 'rasnumer'), ('mot', 'rodimark', 'rasnumer'), ('mot', 'heitisveitar', 'rodimark', 'rasnumer'), ('mot', 'numerflogu', 'rasnumer'), ('mot', 'kyn', 'nafn', 'rasnumer'), ('mot', 'lokatimiklst', 'linunumerfloguskrar', 'nettotimi', 'rasnumer'), ('mot', 'numervaraflogu', 'rasnumer'), ('mot', 'felag', 'kyn', 'nafn', 'rasnumer'), ('skráningardags_rásnúmers', 'skráningartími_rásnúmers', 'kyn', 'nafn', 'netskráning', 'mot', 'rasnumer'), ('úthlutað_rásnúmer', 'kyn', 'nafn', 'mot', 'rasnumer'), ('mot', 'greinnumer', 'rodimark', 'rodinnangreinar', 'rasnumer'), ('mot', 'linunumerfloguskrar', 'rasnumer'),)


class AthlCompetitorsinevent(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mot = models.CharField(primary_key=True, max_length=10)
    greinarnumer = models.IntegerField()
    lina = models.IntegerField()
    grein = models.CharField(max_length=10)
    kyn = models.IntegerField()
    flokkur = models.CharField(max_length=10)
    ridill = models.IntegerField()
    numerridilsekkinotad = models.IntegerField()
    dagsetninggreinar = models.DateTimeField()
    timigreinar = models.DateTimeField()
    rasnumer = models.IntegerField()
    leitarnafn = models.CharField(max_length=30)
    ridillnumer = models.IntegerField()
    stokkkastrod = models.IntegerField()
    nafn = models.CharField(max_length=35)
    faedingarar = models.IntegerField()
    felag = models.CharField(max_length=10)
    timi = models.DecimalField(max_digits=38, decimal_places=20)
    metrar = models.DecimalField(max_digits=38, decimal_places=20)
    vindur = models.DecimalField(max_digits=38, decimal_places=20)
    arangur = models.CharField(max_length=10)
    rafmagnstimataka = models.SmallIntegerField()
    thrautarstig = models.IntegerField()
    urslitarod = models.IntegerField()
    samasaetiognaestiaundan = models.SmallIntegerField()
    nanarirod = models.IntegerField()
    stig = models.DecimalField(max_digits=38, decimal_places=20)
    stadakeppni = models.IntegerField()
    urslitarodtexti = models.CharField(max_length=10)
    iaaf_stig = models.IntegerField(db_column='IAAF Stig')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tilraun1 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur1 = models.DecimalField(max_digits=38, decimal_places=20)
    merking1 = models.IntegerField()
    tilraun2 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur2 = models.DecimalField(max_digits=38, decimal_places=20)
    merking2 = models.IntegerField()
    tilraun3 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur3 = models.DecimalField(max_digits=38, decimal_places=20)
    merking3 = models.IntegerField()
    tilraun4 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur4 = models.DecimalField(max_digits=38, decimal_places=20)
    merking4 = models.IntegerField()
    tilraun5 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur5 = models.DecimalField(max_digits=38, decimal_places=20)
    merking5 = models.IntegerField()
    tilraun6 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur6 = models.DecimalField(max_digits=38, decimal_places=20)
    merking6 = models.IntegerField()
    sortorder1 = models.DecimalField(max_digits=38, decimal_places=20)
    sortorder2 = models.DecimalField(max_digits=38, decimal_places=20)
    seria = models.CharField(max_length=150)
    athugasemd = models.CharField(max_length=20)
    handvirkathugasemd = models.SmallIntegerField()
    nullarangur = models.SmallIntegerField()
    bestiaranguriar = models.DecimalField(max_digits=38, decimal_places=20)
    personulegmet = models.DecimalField(max_digits=38, decimal_places=20)
    bestiaranguriartexti = models.CharField(max_length=15)
    personulegtmettexti = models.CharField(max_length=15)
    rodiundanurslitum = models.IntegerField()
    qualification = models.CharField(max_length=1)
    gestur = models.SmallIntegerField()
    handvirkstig = models.SmallIntegerField()
    rasnumeraskyrslu = models.IntegerField()
    unglingastig = models.IntegerField(db_column='Unglingastig')  # Field name made lowercase.
    performaceremarks = models.CharField(db_column='PerformaceRemarks', max_length=30)  # Field name made lowercase.
    startreactiontime = models.DecimalField(db_column='StartReactionTime', max_digits=38, decimal_places=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$CompetitorsInEvent'
        unique_together = (('mot', 'greinarnumer', 'lina'), ('mot', 'rasnumer', 'stadakeppni', 'dagsetninggreinar', 'timigreinar', 'greinarnumer', 'lina'), ('mot', 'felag', 'kyn', 'flokkur', 'stadakeppni', 'stig', 'greinarnumer', 'lina'), ('mot', 'greinarnumer', 'ridill', 'numerridilsekkinotad', 'stokkkastrod', 'lina'), ('mot', 'greinarnumer', 'urslitarod', 'nanarirod', 'lina'), ('mot', 'rasnumer', 'dagsetninggreinar', 'timigreinar', 'greinarnumer', 'lina'), ('mot', 'greinarnumer', 'timi', 'urslitarod', 'lina'), ('mot', 'greinarnumer', 'sortorder1', 'sortorder2', 'nanarirod', 'lina'), ('mot', 'kyn', 'nafn', 'greinarnumer', 'lina'),)


class AthlCountryCodesIso2And3(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    iso_code_2 = models.CharField(db_column='ISO Code 2', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enskt_heiti = models.CharField(db_column='Enskt heiti', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    iso_code_3 = models.CharField(db_column='ISO Code 3', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nationality = models.CharField(db_column='Nationality', max_length=50)  # Field name made lowercase.
    iso_country_no = models.CharField(db_column='ISO Country No', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    iso_country_no_2 = models.CharField(db_column='ISO Country No - 2', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Country Codes ISO 2 and 3'


class AthlCountyUnion(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    code = models.CharField(db_column='Code', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$County Union'


class AthlCrossRefTableKeys(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    table_entry_no_field = models.IntegerField(db_column='Table Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    enabled = models.SmallIntegerField(db_column='Enabled')  # Field name made lowercase.
    key_list = models.CharField(db_column='Key List', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sum_fields = models.CharField(db_column='Sum Fields', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    key_groups = models.CharField(db_column='Key Groups', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Cross Ref_ Table Keys'
        unique_together = (('table_entry_no_field', 'line_no_field'),)


class AthlCrossReferenceObjectLines(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entry_no_field = models.IntegerField(db_column='Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number')  # Field name made lowercase.
    version = models.IntegerField(db_column='Version')  # Field name made lowercase.
    line = models.CharField(db_column='Line', max_length=250)  # Field name made lowercase.
    line_continue = models.CharField(db_column='Line Continue', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Cross Reference Object Lines'
        unique_together = (('entry_no_field', 'line_no_field'), ('type', 'number', 'version', 'entry_no_field', 'line_no_field'),)


class AthlCrossReferenceObjects(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entry_no_field = models.IntegerField(db_column='Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number')  # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active')  # Field name made lowercase.
    version = models.IntegerField(db_column='Version')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modified_time = models.DateTimeField(db_column='Modified Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    imported_by = models.CharField(db_column='Imported By', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    import_date = models.DateTimeField(db_column='Import Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    import_time = models.DateTimeField(db_column='Import Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    import_file_name = models.CharField(db_column='Import File Name', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Cross Reference Objects'
        unique_together = (('active', 'type', 'number', 'entry_no_field'), ('imported_by', 'import_date', 'import_time', 'import_file_name', 'entry_no_field'), ('active', 'type', 'description', 'entry_no_field'),)


class AthlCrossReferenceProperties(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    table_entry_no_field = models.IntegerField(db_column='Table Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_line_no_field = models.IntegerField(db_column='Field Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    property = models.CharField(db_column='Property', max_length=30)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250)  # Field name made lowercase.
    description_2 = models.CharField(db_column='Description 2', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    resolved = models.SmallIntegerField(db_column='Resolved')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Cross Reference Properties'
        unique_together = (('table_entry_no_field', 'field_line_no_field', 'line_no_field'), ('property', 'table_entry_no_field', 'field_line_no_field', 'line_no_field'), ('table_entry_no_field', 'property', 'resolved', 'field_line_no_field', 'line_no_field'),)


class AthlCrossReferenceTableFields(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entry_no_field = models.IntegerField(db_column='Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    table_id = models.IntegerField(db_column='Table ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version_no_field = models.IntegerField(db_column='Version No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_no_field = models.IntegerField(db_column='Field No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_name = models.CharField(db_column='Field Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_type = models.IntegerField(db_column='Field Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_length = models.IntegerField(db_column='Field Length')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_class = models.IntegerField(db_column='Field Class')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_enabled = models.SmallIntegerField(db_column='Field Enabled')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Cross Reference Table Fields'
        unique_together = (('entry_no_field', 'line_no_field'), ('table_id', 'version_no_field', 'field_no_field', 'entry_no_field', 'line_no_field'), ('entry_no_field', 'field_name', 'line_no_field'),)


class AthlCrossReferenceWhereUsed(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    line_no_field = models.IntegerField(db_column='Line No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    source_type = models.IntegerField(db_column='Source Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    source_object_entry_no_field = models.IntegerField(db_column='Source Object Entry No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_line_no_field = models.IntegerField(db_column='Field Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    target_link_type = models.IntegerField(db_column='Target Link Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    link_id_number = models.IntegerField(db_column='Link ID Number')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    link_version_no_field = models.IntegerField(db_column='Link Version No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    link_entry_no_field = models.IntegerField(db_column='Link Entry No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    link_object_line = models.IntegerField(db_column='Link Object Line')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.
    target_description = models.CharField(db_column='Target Description', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    text = models.CharField(db_column='Text', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Cross Reference Where Used'
        unique_together = (('source_type', 'source_object_entry_no_field', 'field_line_no_field', 'line_no_field'), ('target_link_type', 'link_entry_no_field', 'link_object_line', 'line_no_field'),)


class AthlCurrencyXml(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    date = models.DateTimeField(db_column='Date', primary_key=True)  # Field name made lowercase.
    currcode = models.CharField(db_column='CurrCode', max_length=3)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    source_counter = models.IntegerField(db_column='Source Counter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rate = models.DecimalField(db_column='Rate', max_digits=38, decimal_places=20)  # Field name made lowercase.
    kaupgengi = models.DecimalField(db_column='Kaupgengi', max_digits=38, decimal_places=20)  # Field name made lowercase.
    miðgengi = models.DecimalField(db_column='Miðgengi', max_digits=38, decimal_places=20)  # Field name made lowercase.
    sölugengi = models.DecimalField(db_column='Sölugengi', max_digits=38, decimal_places=20)  # Field name made lowercase.
    heiti = models.CharField(db_column='Heiti', max_length=50)  # Field name made lowercase.
    gengi_obreytt = models.CharField(db_column='Gengi Obreytt', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Currency XML'
        unique_together = (('date', 'currcode', 'type', 'source_counter'), ('source_counter', 'date', 'currcode', 'type'),)


class AthlDagbkSkrningar(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    tími = models.DateTimeField(db_column='Tími')  # Field name made lowercase.
    heiti_móts = models.CharField(db_column='Heiti móts', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dagsetning_móts = models.DateTimeField(db_column='Dagsetning móts')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fjöldi_lína = models.IntegerField(db_column='Fjöldi lína')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    athugasemd = models.CharField(db_column='Athugasemd', max_length=250)  # Field name made lowercase.
    frá_línu_nr_field = models.IntegerField(db_column='Frá línu nr_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    til_línu_nr_field = models.IntegerField(db_column='Til línu nr_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vinna_í_mínútum = models.DecimalField(db_column='Vinna í mínútum', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Dagbók skráningar'
        unique_together = (('dagsetning', 'lína'),)


class AthlDistLocationVersion(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30)  # Field name made lowercase.
    plugin_id = models.CharField(db_column='Plugin ID', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plugin_string = models.CharField(db_column='Plugin String', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Dist_ Location Version'


class AthlDistribIncludeExcludeList(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    scheduler_job_id = models.CharField(db_column='Scheduler Job ID', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_code = models.CharField(db_column='Location Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    time_slot_setup = models.CharField(db_column='Time Slot Setup', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Distrib_ Include_Exclude List'
        unique_together = (('scheduler_job_id', 'location_code'),)


class AthlDistributionGroup(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    group_code = models.CharField(db_column='Group Code', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(db_column='Description', max_length=30)  # Field name made lowercase.
    default_group = models.SmallIntegerField(db_column='Default Group')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    no_filter = models.SmallIntegerField(db_column='No Filter')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Distribution Group'


class AthlDistributionGroupMember(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    group_code = models.CharField(db_column='Group Code', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subgroup_code = models.CharField(db_column='Subgroup Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distrib_loc_code = models.CharField(db_column='Distrib_ Loc_ Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    group_type = models.IntegerField(db_column='Group Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Distribution Group Member'
        unique_together = (('group_code', 'subgroup_code', 'distrib_loc_code'), ('distrib_loc_code', 'group_code', 'subgroup_code'),)


class AthlDistributionList(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    table_id = models.IntegerField(db_column='Table ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    value = models.CharField(db_column='Value', max_length=100)  # Field name made lowercase.
    group_code = models.CharField(db_column='Group Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subgroup_code = models.CharField(db_column='Subgroup Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    store_group = models.CharField(db_column='Store Group', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Distribution List'
        unique_together = (('table_id', 'value', 'group_code', 'subgroup_code'), ('group_code', 'subgroup_code', 'table_id', 'value'),)


class AthlDistributionLocation(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    code = models.CharField(db_column='Code', primary_key=True, max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30)  # Field name made lowercase.
    server_no_field = models.IntegerField(db_column='Server No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    net_type = models.CharField(db_column='Net Type', max_length=13)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    db_path_name = models.CharField(db_column='Db_ Path && Name', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    company_name = models.CharField(db_column='Company Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_id = models.CharField(db_column='User ID', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    password = models.CharField(db_column='Password', max_length=10)  # Field name made lowercase.
    server_name = models.CharField(db_column='Server Name', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    error_in_last_operation = models.SmallIntegerField(db_column='Error in Last Operation')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_operation_error_code = models.IntegerField(db_column='Last Operation Error Code')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tstimeout = models.IntegerField(db_column='TSTimeOut')  # Field name made lowercase.
    developers_license = models.BinaryField(db_column='Developers License', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_user_license = models.BinaryField(db_column='End-User License', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dev_license_expiry_date = models.DateTimeField(db_column='Dev_ License Expiry Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    path_to_finplugin_directory = models.CharField(db_column='Path To FinPlugin Directory', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    active_for_replication = models.SmallIntegerField(db_column='Active for Replication')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    path_to_cfront_directory = models.CharField(db_column='Path To CFront Directory', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_is_head_office = models.SmallIntegerField(db_column='Location Is Head Office')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_uses_server = models.SmallIntegerField(db_column='Location Uses Server')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    use_nt_authentication = models.SmallIntegerField(db_column='Use NT Authentication')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    use_commit_cache = models.SmallIntegerField(db_column='Use Commit Cache')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cache_size = models.IntegerField(db_column='Cache Size')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    driver_name = models.CharField(db_column='Driver Name', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_format = models.CharField(db_column='Date Format', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.CharField(db_column='Version', max_length=10)  # Field name made lowercase.
    blob = models.BinaryField(db_column='Blob', blank=True, null=True)  # Field name made lowercase.
    distribution_group = models.CharField(db_column='Distribution Group', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distribution_server = models.CharField(db_column='Distribution Server', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    connection_string = models.CharField(db_column='Connection String', max_length=120)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_director_password = models.CharField(db_column='Data Director Password', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    forwarder = models.CharField(db_column='Forwarder', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Distribution Location'


class AthlDistributionSubgroup(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    group_code = models.CharField(db_column='Group Code', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subgroup_code = models.CharField(db_column='Subgroup Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(db_column='Description', max_length=30)  # Field name made lowercase.
    no_filter = models.SmallIntegerField(db_column='No Filter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    group_is_distrib_location = models.SmallIntegerField(db_column='Group Is Distrib_ Location')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    default_subgroup = models.SmallIntegerField(db_column='Default Subgroup')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Distribution Subgroup'
        unique_together = (('group_code', 'subgroup_code'),)


class AthlDistributionSublocation(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    distribution_location = models.CharField(db_column='Distribution Location', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code = models.CharField(db_column='Code', max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30)  # Field name made lowercase.
    server_name = models.CharField(db_column='Server Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    db_path_name = models.CharField(db_column='Db_ Path && Name', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    company_name = models.CharField(db_column='Company Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_id = models.CharField(db_column='User ID', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    password = models.CharField(db_column='Password', max_length=10)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=10)  # Field name made lowercase.
    xdistribution_server = models.CharField(db_column='xDistribution Server', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    connection_string = models.CharField(db_column='Connection String', max_length=120)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Distribution Sublocation'
        unique_together = (('distribution_location', 'code'),)


class AthlEntryfeepaymentlines(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    competitioncode = models.CharField(db_column='CompetitionCode', primary_key=True, max_length=10)  # Field name made lowercase.
    club = models.CharField(db_column='Club', max_length=10)  # Field name made lowercase.
    bibno = models.IntegerField(db_column='BibNo')  # Field name made lowercase.
    entrylineno = models.IntegerField(db_column='EntryLineNo')  # Field name made lowercase.
    dateandtime = models.DateTimeField(db_column='DateAndTime')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=38, decimal_places=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.
    competitorsname = models.CharField(db_column='CompetitorsName', max_length=50)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', max_length=50)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$EntryFeePaymentLines'
        unique_together = (('competitioncode', 'club', 'bibno', 'entrylineno'), ('competitioncode', 'club', 'status', 'bibno', 'entrylineno'),)


class AthlEntryfeepaymnets(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entryno = models.IntegerField(db_column='EntryNo', primary_key=True)  # Field name made lowercase.
    competitioncode = models.CharField(db_column='CompetitionCode', max_length=10)  # Field name made lowercase.
    paymentfromclub = models.CharField(db_column='PaymentFromClub', max_length=10)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', max_length=50)  # Field name made lowercase.
    dateandtime = models.DateTimeField(db_column='DateAndTime')  # Field name made lowercase.
    paymentamount = models.DecimalField(db_column='PaymentAmount', max_digits=38, decimal_places=20)  # Field name made lowercase.
    authorisationcode = models.CharField(db_column='AuthorisationCode', max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$EntryFeePaymnets'
        unique_together = (('competitioncode', 'paymentfromclub', 'referenceno', 'entryno'),)


class AthlEvents(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    grein = models.CharField(db_column='Grein', primary_key=True, max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    tegund_greinar = models.IntegerField(db_column='Tegund greinar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nánari_tegundargreining = models.IntegerField(db_column='Nánari tegundargreining')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fjöldi_í_boðhlaupssveit = models.IntegerField(db_column='Fjöldi í boðhlaupssveit')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    krefst_vindmælis = models.SmallIntegerField(db_column='Krefst vindmælis')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesti_löglegi_vindur = models.DecimalField(db_column='Mesti löglegi vindur', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þyngd_kastáhalds = models.DecimalField(db_column='Þyngd kastáhalds', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hæð_grinda = models.DecimalField(db_column='Hæð grinda', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    viðbót_v_handtímatöku = models.DecimalField(db_column='Viðbót v_ handtímatöku', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_í_afrekaskrá = models.DecimalField(db_column='Röð í afrekaskrá', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti = models.CharField(db_column='Heiti', max_length=30)  # Field name made lowercase.
    leitarheiti = models.CharField(db_column='Leitarheiti', max_length=30)  # Field name made lowercase.
    eining = models.CharField(db_column='Eining', max_length=10)  # Field name made lowercase.
    í_venjulegri_afrekaskrá = models.SmallIntegerField(db_column='Í venjulegri afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enskt_heiti_greinar = models.CharField(db_column='Enskt heiti greinar', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enskt_einingarheiti = models.CharField(db_column='Enskt einingarheiti', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stigaútreikningur_reitur_a = models.DecimalField(db_column='Stigaútreikningur - Reitur A', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stigaútreikningur_reitur_b = models.DecimalField(db_column='Stigaútreikningur - Reitur B', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stigaútreikningur_reitur_c = models.DecimalField(db_column='Stigaútreikningur - Reitur C', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tveggja_daga_þraut = models.SmallIntegerField(db_column='Tveggja daga þraut')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sýna_handtímatöku_sér = models.SmallIntegerField(db_column='Sýna handtímatöku sér')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    besti_tími_hlaups = models.CharField(db_column='Besti tími hlaups', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hámarkgildi_tæknigreinar = models.CharField(db_column='Hámarkgildi tæknigreinar', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    greinahópur = models.IntegerField(db_column='Greinahópur')  # Field name made lowercase.
    spretthlaup_á_beinni_braut = models.SmallIntegerField(db_column='Spretthlaup á beinni braut')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þrautargrein_1 = models.CharField(db_column='Þrautargrein 1', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þrautargrein_2 = models.CharField(db_column='Þrautargrein 2', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þrautargrein_3 = models.CharField(db_column='Þrautargrein 3', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þrautargrein_4 = models.CharField(db_column='Þrautargrein 4', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þrautargrein_5 = models.CharField(db_column='Þrautargrein 5', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þrautargrein_6 = models.CharField(db_column='Þrautargrein 6', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þrautargrein_7 = models.CharField(db_column='Þrautargrein 7', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þrautargrein_8 = models.CharField(db_column='Þrautargrein 8', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þrautargrein_9 = models.CharField(db_column='Þrautargrein 9', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þrautargrein_10 = models.CharField(db_column='Þrautargrein 10', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skrá_íslandsmet = models.SmallIntegerField(db_column='Skrá Íslandsmet')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_í_þraut = models.IntegerField(db_column='Röð í þraut')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleppa_í_afrekaskrá = models.SmallIntegerField(db_column='Sleppa í afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_frá_fyrir_2011_field = models.IntegerField(db_column='Aldur frá (fyrir 2011)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    aldur_til_fyrir_2011_field = models.IntegerField(db_column='Aldur til (fyrir 2011)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bókarmerki = models.CharField(db_column='Bókarmerki', max_length=30)  # Field name made lowercase.
    greinarheiti_í_kerfi_breiðabli = models.CharField(db_column='Greinarheiti í kerfi Breiðabli', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dagsetningartakmörkun = models.CharField(db_column='Dagsetningartakmörkun', max_length=30)  # Field name made lowercase.
    vegal_götuhlaups_í_km = models.DecimalField(db_column='Vegal_ götuhlaups í km', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldurflokkasía_öldunga = models.CharField(db_column='Aldurflokkasía öldunga', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stigagrein_skv_iaaf = models.SmallIntegerField(db_column='Stigagrein skv_ IAAF')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lengd_hlaups_í_metrum = models.IntegerField(db_column='Lengd hlaups í metrum')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    teg_hlaups_v_fj_brauta = models.IntegerField(db_column='Teg_ hlaups v_ fj_ brauta')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ensk_skammstöfun_greinar = models.CharField(db_column='Ensk skammstöfun greinar', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_greinar = models.CharField(db_column='Tákn Greinar', max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mælieining = models.CharField(db_column='Mælieining', max_length=10)  # Field name made lowercase.
    aldurssía = models.CharField(db_column='Aldurssía', max_length=30)  # Field name made lowercase.
    aldur_frá = models.IntegerField(db_column='Aldur frá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_til = models.IntegerField(db_column='Aldur til')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eventcode = models.CharField(db_column='EventCode', max_length=10)  # Field name made lowercase.
    samsettur_lykill = models.CharField(db_column='Samsettur lykill', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eventcodeforregistration = models.CharField(db_column='EventCodeForRegistration', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Events'
        unique_together = (('grein', 'kyn', 'flokkur', 'úti_inni'), ('röð_í_afrekaskrá', 'grein', 'kyn', 'flokkur', 'úti_inni'), ('heiti', 'grein', 'kyn', 'flokkur', 'úti_inni'), ('viðbót_v_handtímatöku', 'grein', 'kyn', 'flokkur', 'úti_inni'), ('bókarmerki', 'grein', 'kyn', 'flokkur', 'úti_inni'), ('greinarheiti_í_kerfi_breiðabli', 'grein', 'kyn', 'flokkur', 'úti_inni'), ('lengd_hlaups_í_metrum', 'grein', 'kyn', 'flokkur', 'úti_inni'), ('ensk_skammstöfun_greinar', 'grein', 'kyn', 'flokkur', 'úti_inni'), ('aldur_til', 'grein', 'kyn', 'flokkur', 'úti_inni'), ('kyn', 'greinahópur', 'grein', 'flokkur', 'úti_inni'), ('samsettur_lykill', 'röð_í_afrekaskrá', 'grein', 'kyn', 'flokkur', 'úti_inni'), ('eventcode', 'kyn', 'úti_inni', 'grein', 'flokkur'),)


class AthlEventsincompetition(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mot = models.CharField(primary_key=True, max_length=10)
    greinnumer = models.IntegerField()
    grein = models.CharField(max_length=10)
    kyn = models.IntegerField()
    flokkur = models.CharField(max_length=10)
    utiinni = models.IntegerField()
    heitigreinar = models.CharField(max_length=70)
    yngstikeppandi = models.IntegerField()
    elstikeppandi = models.IntegerField()
    keppnisflokkur = models.CharField(max_length=10)
    rodiafrekaskra = models.DecimalField(max_digits=38, decimal_places=20)
    ridilledaurslit = models.IntegerField()
    dagsetninggreinar = models.DateTimeField()
    ensktheitigreinar = models.CharField(max_length=70)
    aldursfloldunga = models.CharField(max_length=10)
    stadur = models.CharField(max_length=30)
    timi = models.DateTimeField()
    dagsetning_og_tími = models.DateTimeField(db_column='Dagsetning og tími')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$EventsInCompetition'
        unique_together = (('mot', 'greinnumer'), ('mot', 'kyn', 'keppnisflokkur', 'rodiafrekaskra', 'ridilledaurslit', 'greinnumer'), ('mot', 'stadur', 'greinnumer'), ('grein', 'kyn', 'flokkur', 'utiinni', 'mot', 'greinnumer'), ('mot', 'kyn', 'rodiafrekaskra', 'ridilledaurslit', 'greinnumer'),)


class AthlExcelskjalFrIdega(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_ID')  # Field name made lowercase.
    user_display_name = models.CharField(db_column='User Display Name', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_first_name = models.CharField(db_column='User First Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_middle_name = models.CharField(db_column='User Middle Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_last_name = models.CharField(db_column='User Last Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_personal_id = models.CharField(db_column='User Personal ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gender = models.CharField(db_column='Gender', max_length=10)  # Field name made lowercase.
    user_date_of_birth = models.CharField(db_column='User Date of Birth', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_nationality = models.CharField(db_column='User Nationality', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address_street_name = models.CharField(db_column='Address Street Name', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address_street_number = models.CharField(db_column='Address Street Number', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address_postal_code = models.CharField(db_column='Address Postal Code', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address_city = models.CharField(db_column='Address City', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address_postal_address = models.CharField(db_column='Address Postal Address', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address_country = models.CharField(db_column='Address Country', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    home_phone_no = models.CharField(db_column='Home Phone No', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mobile_phone_no = models.CharField(db_column='Mobile Phone No', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    e_mail = models.CharField(db_column='E-mail', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_entry_no = models.IntegerField(db_column='Run Entry No')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ic_group_id_run = models.CharField(db_column='IC Group ID Run', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_name = models.CharField(db_column='Run Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ic_group_id_year = models.CharField(db_column='IC Group ID Year', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    ic_gropu_distance = models.CharField(db_column='IC Gropu Distance', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distance = models.CharField(db_column='Distance', max_length=30)  # Field name made lowercase.
    ic_group_id_group = models.CharField(db_column='IC Group ID Group', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gender_age_group = models.CharField(db_column='Gender Age Group', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initiation_date = models.CharField(db_column='Initiation Date', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    participant_number = models.IntegerField(db_column='Participant Number')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_group_name = models.CharField(db_column='Run Group Name', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_time = models.CharField(db_column='Run Time', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chip_time = models.CharField(db_column='Chip Time', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_chip_number = models.CharField(db_column='Run Chip Number', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_chip_ownership_status = models.CharField(db_column='Run Chip Ownership Status', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_chip_bunch_no = models.CharField(db_column='Run Chip Bunch No', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pay_method = models.CharField(db_column='Pay Method', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    paid_amount = models.DecimalField(db_column='Paid Amount', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shirt_size = models.CharField(db_column='Shirt Size', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transport_ordered = models.CharField(db_column='Transport Ordered', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    charity_organization_id = models.IntegerField(db_column='Charity Organization ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    charity_name = models.CharField(db_column='Charity Name', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    may_sponsor_contact = models.CharField(db_column='May Sponsor Contact', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    department_name = models.CharField(db_column='Department Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    domestic_travel_support = models.CharField(db_column='Domestic Travel Support', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    international_travel_support = models.CharField(db_column='International Travel Support', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Excelskjal frá Idega'
        unique_together = (('participant_number', 'lína'),)


class AthlFjldittakendaRmFrUpp(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    ár = models.IntegerField(db_column='Ár', primary_key=True)  # Field name made lowercase.
    vegalengd = models.IntegerField(db_column='Vegalengd')  # Field name made lowercase.
    íslenskir_karlar = models.IntegerField(db_column='Íslenskir karlar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    íslenskar_konur = models.IntegerField(db_column='Íslenskar konur')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    erlendir_karlar = models.IntegerField(db_column='Erlendir karlar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    erlendar_konur = models.IntegerField(db_column='Erlendar konur')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fjöldi_sveita = models.IntegerField(db_column='Fjöldi sveita')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fjöldi_pr_sveit = models.IntegerField(db_column='Fjöldi pr_ sveit')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Fjöldi þáttakenda í RM frá upp'
        unique_together = (('ár', 'vegalengd'),)


class AthlFlokkar(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    númer = models.CharField(db_column='Númer', primary_key=True, max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    aldur_frá = models.IntegerField(db_column='Aldur frá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_til = models.IntegerField(db_column='Aldur Til')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti = models.CharField(db_column='Heiti', max_length=30)  # Field name made lowercase.
    skammstöfun = models.CharField(db_column='Skammstöfun', max_length=10)  # Field name made lowercase.
    aldursflokkur = models.SmallIntegerField(db_column='Aldursflokkur')  # Field name made lowercase.
    þágufallsheiti = models.CharField(db_column='Þágufallsheiti', max_length=30)  # Field name made lowercase.
    leitarheiti = models.CharField(db_column='Leitarheiti', max_length=30)  # Field name made lowercase.
    röð_í_afrekaskrá = models.IntegerField(db_column='Röð í afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_frá_í_afrekaskrá_field = models.IntegerField(db_column='Aldur frá (í afrekaskrá)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    aldur_til_í_afrekaskrá_field = models.IntegerField(db_column='Aldur til (í afrekaskrá)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    enskt_heiti_aldursflokks = models.CharField(db_column='Enskt heiti aldursflokks', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    flokkaafmörkun_v_afrekaskrá = models.CharField(db_column='Flokkaafmörkun v_ afrekaskrá', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lína_í_afrekaskrá_html = models.IntegerField(db_column='Lína í afrekaskrá HTML')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    viðbótarstafur_skráa_í_afr_skr = models.CharField(db_column='Viðbótarstafur skráa í afr_skr', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enskt_heiti_stutt_field = models.CharField(db_column='Enskt heiti (stutt)', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    birta_iaaf_stig = models.SmallIntegerField(db_column='Birta IAAF stig')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Flokkar'
        unique_together = (('leitarheiti', 'númer'), ('kyn', 'aldur_frá', 'aldur_til', 'númer'), ('röð_í_afrekaskrá', 'númer'), ('lína_í_afrekaskrá_html', 'númer'), ('kyn', 'aldur_til_í_afrekaskrá_field', 'númer'),)


class AthlFlokkurHlaupsRsnmerabil(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    flokkur_hlaups = models.CharField(db_column='Flokkur hlaups', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_frá = models.IntegerField(db_column='Rásnúmer frá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_til = models.IntegerField(db_column='Rásnúmer til')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_hlaups = models.CharField(db_column='Tákn hlaups', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Flokkur hlaups - Rásnúmerabil'
        unique_together = (('flokkur_hlaups', 'rásnúmer_frá'),)


class AthlFlgurSemEkkiFunduHlGhl13(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    flokkur_hlaups = models.CharField(db_column='Flokkur hlaups', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    flögunúmer = models.CharField(db_column='Flögunúmer', max_length=10)  # Field name made lowercase.
    starttími = models.CharField(db_column='Starttími', max_length=11)  # Field name made lowercase.
    millitími_1 = models.CharField(db_column='Millitími 1', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    millitími_2 = models.CharField(db_column='Millitími 2', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    millitími_3 = models.CharField(db_column='Millitími 3', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    millitími_4 = models.CharField(db_column='Millitími 4', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    millitími_5 = models.CharField(db_column='Millitími 5', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    millitími_6 = models.CharField(db_column='Millitími 6', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    millitími_7 = models.CharField(db_column='Millitími 7', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lokatími = models.CharField(db_column='Lokatími', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Flögur sem ekki fundu hl GHL13'
        unique_together = (('flokkur_hlaups', 'flögunúmer'),)


class AthlFlgurSemEkkiFunduHlaupara(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    flokkur_hlaups = models.CharField(db_column='Flokkur hlaups', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    flögunúmer = models.CharField(db_column='Flögunúmer', max_length=10)  # Field name made lowercase.
    starttími = models.CharField(db_column='Starttími', max_length=11)  # Field name made lowercase.
    millitími_1 = models.CharField(db_column='Millitími 1', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    millitími_2 = models.CharField(db_column='Millitími 2', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    millitími_3 = models.CharField(db_column='Millitími 3', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    millitími_4 = models.CharField(db_column='Millitími 4', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    millitími_5 = models.CharField(db_column='Millitími 5', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    millitími_6 = models.CharField(db_column='Millitími 6', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    millitími_7 = models.CharField(db_column='Millitími 7', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lokatími = models.CharField(db_column='Lokatími', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Flögur sem ekki fundu hlaupara'
        unique_together = (('flokkur_hlaups', 'flögunúmer'),)


class AthlFrjlsrttakerfiUppsetning(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lykill = models.CharField(db_column='Lykill', primary_key=True, max_length=10)  # Field name made lowercase.
    slóð_html_mynda = models.CharField(db_column='Slóð HTML mynda', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_lista_og_xml_textaskrár_field = models.CharField(db_column='Slóð lista og XML (textaskrár)', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    slóð_html_fyrir_innanh_sjónv = models.CharField(db_column='Slóð HTML fyrir innanh_ sjónv', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_rtf_skráa = models.CharField(db_column='Slóð RTF skráa', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    merki_frjálsíþróttasambandsins = models.BinaryField(db_column='Merki Frjálsíþróttasambandsins', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_html_skráa = models.CharField(db_column='Slóð HTML skráa', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    til_er_html_fyrir_mót_eftir_þ_field = models.DateTimeField(db_column='Til er HTML fyrir mót eftir þ_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    núverandi_afrekaskrárár = models.CharField(db_column='Núverandi afrekaskrárár', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    staðsetning_innlestrarskráa = models.CharField(db_column='Staðsetning innlestrarskráa', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_html_skráa_ensk_útgáfa = models.CharField(db_column='Slóð HTML skráa ensk útgáfa', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sjálfgefið_félag_skrán_línur_field = models.CharField(db_column='Sjálfgefið félag (skrán_línur)', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    slóð_úrslitaskráa_f_töflu = models.CharField(db_column='Slóð úrslitaskráa f_ töflu', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    síðasta_uppfærða_action = models.IntegerField(db_column='Síðasta uppfærða Action')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_skráa_keppenda = models.CharField(db_column='Slóð skráa keppenda', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_skráa_keppenda_ensk = models.CharField(db_column='Slóð skráa keppenda ensk', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_skráa_félaga = models.CharField(db_column='Slóð skráa félaga', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_skráa_félaga_ensk = models.CharField(db_column='Slóð skráa félaga ensk', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_1999 = models.CharField(db_column='Afrek 1999', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_1999_ensk = models.CharField(db_column='Afrek 1999 ensk', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2000 = models.CharField(db_column='Afrek 2000', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2000_ensk = models.CharField(db_column='Afrek 2000 ensk', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2001 = models.CharField(db_column='Afrek 2001', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2001_ensk = models.CharField(db_column='Afrek 2001 ensk', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2002 = models.CharField(db_column='Afrek 2002', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2002_ensk = models.CharField(db_column='Afrek 2002 ensk', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2003 = models.CharField(db_column='Afrek 2003', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2003_ensk = models.CharField(db_column='Afrek 2003 ensk', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2004 = models.CharField(db_column='Afrek 2004', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2004_ensk = models.CharField(db_column='Afrek 2004 ensk', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2005 = models.CharField(db_column='Afrek 2005', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2005_ensk = models.CharField(db_column='Afrek 2005 ensk', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rót_afrekaskrár = models.CharField(db_column='Rót afrekaskrár', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_klukkuskráa = models.CharField(db_column='Slóð klukkuskráa', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    númeraröð_keppenda = models.CharField(db_column='Númeraröð keppenda', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2006 = models.CharField(db_column='Afrek 2006', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    afrek_2006_ensk = models.CharField(db_column='Afrek 2006 ensk', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    númerasería_myndaskráar = models.CharField(db_column='Númerasería myndaskráar', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    land_við_útr_á_unglingastigum = models.CharField(db_column='Land við útr_ á Unglingastigum', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_á_ultrak_499_klukkuskrár = models.CharField(db_column='Slóð á Ultrak 499 klukkuskrár', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_á_lynx_tímtökuklukkur = models.CharField(db_column='Slóð á Lynx tímtökuklukkur', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_á_xml_skrán_skrár_f_ruv = models.CharField(db_column='Slóð á XML Skrán_skrár f_ RUV', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_á_xml_úrsl_skrár_f_ruv = models.CharField(db_column='Slóð á XML Úrsl_skrár f_ RUV', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dags_hlaupa_f_afh_rásnúmera = models.DateTimeField(db_column='Dags_ hlaupa f_ afh_ rásnúmera')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    velja_vegalengdir_f_nýskránin = models.IntegerField(db_column='Velja vegalengdir f_ nýskránin')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_móts_fyrir_scoreboard = models.CharField(db_column='Tákn móts fyrir scoreboard', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sýna_stigastöðu_í_flokki = models.IntegerField(db_column='Sýna stigastöðu í flokki')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nota_fæðingarár_innri_breyta_field = models.SmallIntegerField(db_column='Nota fæðingarár (innri breyta)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    síðasta_backup_dags_innri_bre = models.DateTimeField(db_column='Síðasta backup dags (innri bre')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    síðasta_backup_tími_innri_bre = models.DateTimeField(db_column='Síðasta backup tími (innri bre')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fj_mánuða_fyrir_ársbesta = models.IntegerField(db_column='Fj_ mánuða fyrir ársbesta')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fj_daga_fyrir_ársbesta = models.IntegerField(db_column='Fj_ daga fyrir ársbesta')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prós_pr_ár_að_bæta_við_pers_field = models.DecimalField(db_column='Prós_ pr_ ár að bæta við pers_', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'Athl$Frjálsíþróttakerfi uppsetning'


class AthlGuidFyrirKeppendurGsse2015(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót = models.CharField(db_column='Mót', primary_key=True, max_length=10)  # Field name made lowercase.
    rásnúmer = models.IntegerField(db_column='Rásnúmer')  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=50)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$GUID fyrir keppendur GSSE2015'
        unique_together = (('mót', 'rásnúmer'),)


class AthlGamalRtfTaflan(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    pur = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Athl$Gamal RTF taflan'


class AthlGamesrecords(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entryno = models.IntegerField(db_column='EntryNo', primary_key=True)  # Field name made lowercase.
    competitiontypecode = models.CharField(db_column='CompetitionTypeCode', max_length=10)  # Field name made lowercase.
    eventcode = models.CharField(db_column='EventCode', max_length=10)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender')  # Field name made lowercase.
    agegroupcode = models.CharField(db_column='AgeGroupCode', max_length=10)  # Field name made lowercase.
    outdoorsindoors = models.IntegerField(db_column='OutdoorsIndoors')  # Field name made lowercase.
    ageto = models.IntegerField(db_column='AgeTo')  # Field name made lowercase.
    gamesrecorddate = models.DateTimeField(db_column='GamesRecordDate')  # Field name made lowercase.
    gamesrecordperformance = models.CharField(db_column='GamesRecordPerformance', max_length=20)  # Field name made lowercase.
    competitorcode = models.CharField(db_column='CompetitorCode', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    club = models.CharField(db_column='Club', max_length=10)  # Field name made lowercase.
    windreading = models.DecimalField(db_column='WindReading', max_digits=38, decimal_places=20)  # Field name made lowercase.
    competitionvenue = models.CharField(db_column='CompetitionVenue', max_length=80)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=80)  # Field name made lowercase.
    competitioncode = models.CharField(db_column='CompetitionCode', max_length=10)  # Field name made lowercase.
    eventlineno = models.IntegerField(db_column='EventLineNo')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    yearofbirth = models.IntegerField(db_column='YearOfBirth')  # Field name made lowercase.
    previousgamesrecord = models.CharField(db_column='PreviousGamesRecord', max_length=20)  # Field name made lowercase.
    previousgamesrecdate = models.DateTimeField(db_column='PreviousGamesRecDate')  # Field name made lowercase.
    previousgamsrecholder = models.CharField(db_column='PreviousGamsRecHolder', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$GamesRecords'
        unique_together = (('entryno', 'competitiontypecode', 'eventcode', 'gender', 'agegroupcode', 'outdoorsindoors', 'ageto', 'eventlineno'), ('competitioncode', 'eventlineno', 'entryno'),)


class AthlGamlarSkannaarFlgur(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    tölva = models.CharField(db_column='Tölva', primary_key=True, max_length=50)  # Field name made lowercase.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    númer_flögu = models.CharField(db_column='Númer flögu', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    innra_rásnúmer = models.IntegerField(db_column='Innra rásnúmer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nafn = models.CharField(db_column='Nafn', max_length=50)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    aldursflokkur = models.CharField(db_column='Aldursflokkur', max_length=30)  # Field name made lowercase.
    land = models.CharField(db_column='Land', max_length=10)  # Field name made lowercase.
    heiti_sveitar = models.CharField(db_column='Heiti sveitar', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nafn_ekki_komið = models.SmallIntegerField(db_column='Nafn ekki komið')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mótafilter = models.CharField(db_column='Mótafilter', max_length=100)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    tími = models.DateTimeField(db_column='Tími')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Gamlar Skannaðar flögur'
        unique_together = (('tölva', 'lína'),)


class AthlGeneralLedgerSetup(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    primary_key = models.CharField(db_column='Primary Key', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allow_posting_from = models.DateTimeField(db_column='Allow Posting From')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allow_posting_to = models.DateTimeField(db_column='Allow Posting To')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pmt_disc_excl_vat = models.SmallIntegerField(db_column='Pmt_ Disc_ Excl_ VAT')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unrealized_vat = models.SmallIntegerField(db_column='Unrealized VAT')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adjust_for_payment_disc_field = models.SmallIntegerField(db_column='Adjust for Payment Disc_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mark_cr_memos_as_corrections = models.SmallIntegerField(db_column='Mark Cr_ Memos as Corrections')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    local_address_format = models.IntegerField(db_column='Local Address Format')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inv_rounding_precision_lcy_field = models.DecimalField(db_column='Inv_ Rounding Precision (LCY)', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    inv_rounding_type_lcy_field = models.IntegerField(db_column='Inv_ Rounding Type (LCY)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    local_cont_addr_format = models.IntegerField(db_column='Local Cont_ Addr_ Format')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bank_account_nos_field = models.CharField(db_column='Bank Account Nos_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    recalculate_sales_tax = models.SmallIntegerField(db_column='Recalculate Sales Tax')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    summarize_g_l_entries = models.SmallIntegerField(db_column='Summarize G_L Entries')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amount_decimal_places = models.CharField(db_column='Amount Decimal Places', max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unit_amount_decimal_places = models.CharField(db_column='Unit-Amount Decimal Places', max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    additional_reporting_currency = models.CharField(db_column='Additional Reporting Currency', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vat_tolerance_field = models.DecimalField(db_column='VAT Tolerance %', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    emu_currency = models.SmallIntegerField(db_column='EMU Currency')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lcy_code = models.CharField(db_column='LCY Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vat_exchange_rate_adjustment = models.IntegerField(db_column='VAT Exchange Rate Adjustment')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amount_rounding_precision = models.DecimalField(db_column='Amount Rounding Precision', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unit_amount_rounding_precision = models.DecimalField(db_column='Unit-Amount Rounding Precision', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    appln_rounding_precision = models.DecimalField(db_column='Appln_ Rounding Precision', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$General Ledger Setup'


class AthlGrunnurFyrirStigatWmapldun(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    vegalengd = models.DecimalField(db_column='Vegalengd', max_digits=38, decimal_places=20)  # Field name made lowercase.
    opinn_staðall = models.DecimalField(db_column='Opinn staðall', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_5_ára = models.DecimalField(db_column='5 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_6_ára = models.DecimalField(db_column='6 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_7_ára = models.DecimalField(db_column='7 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_8_ára = models.DecimalField(db_column='8 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_9_ára = models.DecimalField(db_column='9 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10_ára = models.DecimalField(db_column='10 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_11_ára = models.DecimalField(db_column='11 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_ára = models.DecimalField(db_column='12 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_13_ára = models.DecimalField(db_column='13 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_14_ára = models.DecimalField(db_column='14 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15_ára = models.DecimalField(db_column='15 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_16_ára = models.DecimalField(db_column='16 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_ára = models.DecimalField(db_column='17 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_18_ára = models.DecimalField(db_column='18 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_19_ára = models.DecimalField(db_column='19 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_20_ára = models.DecimalField(db_column='20 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_21_ára = models.DecimalField(db_column='21 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_22_ára = models.DecimalField(db_column='22 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_23_ára = models.DecimalField(db_column='23 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_24_ára = models.DecimalField(db_column='24 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_25_ára = models.DecimalField(db_column='25 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_26_ára = models.DecimalField(db_column='26 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_27_ára = models.DecimalField(db_column='27 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_28_ára = models.DecimalField(db_column='28 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_29_ára = models.DecimalField(db_column='29 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_30_ára = models.DecimalField(db_column='30 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_31_ára = models.DecimalField(db_column='31 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_32_ára = models.DecimalField(db_column='32 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_33_ára = models.DecimalField(db_column='33 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_34_ára = models.DecimalField(db_column='34 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_35_ára = models.DecimalField(db_column='35 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_36_ára = models.DecimalField(db_column='36 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_37_ára = models.DecimalField(db_column='37 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_38_ára = models.DecimalField(db_column='38 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_39_ára = models.DecimalField(db_column='39 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_40_ára = models.DecimalField(db_column='40 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_41_ára = models.DecimalField(db_column='41 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_42_ára = models.DecimalField(db_column='42 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_43_ára = models.DecimalField(db_column='43 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_44_ára = models.DecimalField(db_column='44 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_45_ára = models.DecimalField(db_column='45 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_46_ára = models.DecimalField(db_column='46 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_47_ára = models.DecimalField(db_column='47 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_48_ára = models.DecimalField(db_column='48 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_49_ára = models.DecimalField(db_column='49 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_50_ára = models.DecimalField(db_column='50 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_51_ára = models.DecimalField(db_column='51 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_52_ára = models.DecimalField(db_column='52 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_53_ára = models.DecimalField(db_column='53 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_54_ára = models.DecimalField(db_column='54 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_55_ára = models.DecimalField(db_column='55 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_56_ára = models.DecimalField(db_column='56 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_57_ára = models.DecimalField(db_column='57 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_58_ára = models.DecimalField(db_column='58 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_59_ára = models.DecimalField(db_column='59 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_60_ára = models.DecimalField(db_column='60 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_61_ára = models.DecimalField(db_column='61 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_62_ára = models.DecimalField(db_column='62 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_63_ára = models.DecimalField(db_column='63 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_64_ára = models.DecimalField(db_column='64 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_65_ára = models.DecimalField(db_column='65 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_66_ára = models.DecimalField(db_column='66 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_67_ára = models.DecimalField(db_column='67 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_68_ára = models.DecimalField(db_column='68 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_69_ára = models.DecimalField(db_column='69 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_70_ára = models.DecimalField(db_column='70 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_71_ára = models.DecimalField(db_column='71 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_72_ára = models.DecimalField(db_column='72 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_73_ára = models.DecimalField(db_column='73 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_74_ára = models.DecimalField(db_column='74 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_75_ára = models.DecimalField(db_column='75 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_76_ára = models.DecimalField(db_column='76 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_77_ára = models.DecimalField(db_column='77 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_78_ára = models.DecimalField(db_column='78 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_79_ára = models.DecimalField(db_column='79 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_80_ára = models.DecimalField(db_column='80 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_81_ára = models.DecimalField(db_column='81 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_82_ára = models.DecimalField(db_column='82 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_83_ára = models.DecimalField(db_column='83 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_84_ára = models.DecimalField(db_column='84 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_85_ára = models.DecimalField(db_column='85 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_86_ára = models.DecimalField(db_column='86 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_87_ára = models.DecimalField(db_column='87 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_88_ára = models.DecimalField(db_column='88 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_89_ára = models.DecimalField(db_column='89 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_90_ára = models.DecimalField(db_column='90 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_91_ára = models.DecimalField(db_column='91 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_92_ára = models.DecimalField(db_column='92 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_93_ára = models.DecimalField(db_column='93 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_94_ára = models.DecimalField(db_column='94 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_95_ára = models.DecimalField(db_column='95 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_96_ára = models.DecimalField(db_column='96 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_97_ára = models.DecimalField(db_column='97 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_98_ára = models.DecimalField(db_column='98 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_99_ára = models.DecimalField(db_column='99 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_100_ára = models.DecimalField(db_column='100 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    gildir_frá_ári = models.IntegerField(db_column='Gildir frá ári', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Grunnur fyrir stigat WMApöldun'
        unique_together = (('gildir_frá_ári', 'grein', 'kyn', 'flokkur', 'úti_inni'), ('grein', 'kyn', 'flokkur', 'úti_inni', 'gildir_frá_ári'),)


class AthlHeightsinhjandpv(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót = models.CharField(db_column='Mót', primary_key=True, max_length=10)  # Field name made lowercase.
    greinarnúmer = models.IntegerField(db_column='Greinarnúmer')  # Field name made lowercase.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    rásnúmer = models.IntegerField(db_column='Rásnúmer')  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=10)  # Field name made lowercase.
    úrslitaröð = models.IntegerField(db_column='Úrslitaröð')  # Field name made lowercase.
    nánari_röð = models.IntegerField(db_column='Nánari röð')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sama_sæti_og_næsti_á_undan = models.SmallIntegerField(db_column='Sama sæti og næsti á undan')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_1_hæð = models.CharField(db_column='1_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2_hæð = models.CharField(db_column='2_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_hæð = models.CharField(db_column='3_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_4_hæð = models.CharField(db_column='4_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_hæð = models.CharField(db_column='5_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_6_hæð = models.CharField(db_column='6_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_7_hæð = models.CharField(db_column='7_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_8_hæð = models.CharField(db_column='8_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_9_hæð = models.CharField(db_column='9_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10_hæð = models.CharField(db_column='10_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_11_hæð = models.CharField(db_column='11_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_hæð = models.CharField(db_column='12_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_13_hæð = models.CharField(db_column='13_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_14_hæð = models.CharField(db_column='14_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15_hæð = models.CharField(db_column='15_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_16_hæð = models.CharField(db_column='16_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_hæð = models.CharField(db_column='17_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_18_hæð = models.CharField(db_column='18_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_19_hæð = models.CharField(db_column='19_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_20_hæð = models.CharField(db_column='20_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_21_hæð = models.CharField(db_column='21_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_22_hæð = models.CharField(db_column='22_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_23_hæð = models.CharField(db_column='23_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_24_hæð = models.CharField(db_column='24_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_25_hæð = models.CharField(db_column='25_ hæð', max_length=3)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    raðsvæði_1_1000_hæð_field = models.IntegerField(db_column='Raðsvæði 1 (1000 - hæð)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    raðsvæði_2_yfir_í_tilraun_field = models.IntegerField(db_column='Raðsvæði 2 (yfir í tilraun)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    raðsvæði_3_fjöldi_falla_field = models.IntegerField(db_column='Raðsvæði 3 (fjöldi falla)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    iaaf_stig = models.IntegerField(db_column='IAAF Stig')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unglingastig = models.IntegerField(db_column='Unglingastig')  # Field name made lowercase.
    openingheight = models.CharField(db_column='OpeningHeight', max_length=10)  # Field name made lowercase.
    firstincreaseby = models.CharField(db_column='FirstIncreaseBy', max_length=10)  # Field name made lowercase.
    firstlimit = models.CharField(db_column='FirstLimit', max_length=10)  # Field name made lowercase.
    secondincreaseby = models.CharField(db_column='SecondIncreaseBy', max_length=10)  # Field name made lowercase.
    secondlimit = models.CharField(db_column='SecondLimit', max_length=10)  # Field name made lowercase.
    thirdincreaseby = models.CharField(db_column='ThirdIncreaseBy', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$HeightsInHJandPV'
        unique_together = (('mót', 'greinarnúmer', 'lína'), ('mót', 'greinarnúmer', 'raðsvæði_1_1000_hæð_field', 'raðsvæði_2_yfir_í_tilraun_field', 'raðsvæði_3_fjöldi_falla_field', 'lína'),)


class AthlHeitiGreinarBreiabKerfi(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    grein = models.CharField(db_column='Grein', primary_key=True, max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    heiti_greinar_frá_breiðabliki = models.CharField(db_column='Heiti Greinar frá Breiðabliki', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ridill = models.IntegerField(db_column='Ridill')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Heiti greinar í Breiðab_kerfi'
        unique_together = (('grein', 'kyn', 'flokkur', 'úti_inni', 'lína'), ('heiti_greinar_frá_breiðabliki', 'grein', 'kyn', 'flokkur', 'úti_inni', 'lína'),)


class AthlHlaupasera(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    tákn = models.CharField(db_column='Tákn', primary_key=True, max_length=10)  # Field name made lowercase.
    heiti = models.CharField(db_column='Heiti', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Hlaupasería'


class AthlIaafStigKeppandafilter(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    mót = models.CharField(db_column='Mót', max_length=10)  # Field name made lowercase.
    grein_númer = models.IntegerField(db_column='Grein númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    raðsvæði = models.DecimalField(db_column='Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase.
    iaaf_stig = models.DecimalField(db_column='IAAF Stig', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meðaltal = models.DecimalField(db_column='Meðaltal', max_digits=38, decimal_places=20)  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=10)  # Field name made lowercase.
    nafn_keppanda = models.CharField(db_column='Nafn keppanda', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meðaltal_móts = models.DecimalField(db_column='Meðaltal móts', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    aldur = models.IntegerField(db_column='Aldur')  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    unglingastig = models.IntegerField(db_column='Unglingastig')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$IAAF stig keppandafilter'
        unique_together = (('iaaf_stig', 'lína'), ('unglingastig', 'lína'), ('keppandanúmer', 'iaaf_stig', 'lína'),)


class AthlIaafStigMts(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót = models.CharField(db_column='Mót', primary_key=True, max_length=10)  # Field name made lowercase.
    grein_númer = models.IntegerField(db_column='Grein númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    raðsvæði = models.DecimalField(db_column='Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase.
    iaaf_stig = models.DecimalField(db_column='IAAF Stig', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meðaltal = models.DecimalField(db_column='Meðaltal', max_digits=38, decimal_places=20)  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=10)  # Field name made lowercase.
    nafn_keppanda = models.CharField(db_column='Nafn keppanda', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meðaltal_móts = models.DecimalField(db_column='Meðaltal móts', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$IAAF stig móts'
        unique_together = (('mót', 'grein_númer', 'lína'), ('mót', 'iaaf_stig', 'grein_númer', 'lína'),)


class AthlIaafpointstable(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    útgáfuár = models.IntegerField(db_column='Útgáfuár', primary_key=True)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    árangur_tími_field = models.DecimalField(db_column='Árangur (Tími)', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    árangur_metrar_field = models.DecimalField(db_column='Árangur (Metrar)', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    stig = models.IntegerField(db_column='Stig')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$IAAFPointsTable'
        unique_together = (('útgáfuár', 'grein', 'kyn', 'flokkur', 'úti_inni', 'árangur_tími_field', 'árangur_metrar_field'), ('útgáfuár', 'grein', 'kyn', 'flokkur', 'úti_inni', 'stig', 'árangur_tími_field', 'árangur_metrar_field'),)


class AthlInnlesnirTmarFrKlukku(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót_götuhlaup = models.CharField(db_column='Mót _ Götuhlaup', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    tími_númer = models.IntegerField(db_column='Tími númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tími = models.IntegerField(db_column='Tími')  # Field name made lowercase.
    tími_2 = models.CharField(db_column='Tími 2', max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð = models.IntegerField(db_column='Röð')  # Field name made lowercase.
    tékktími = models.SmallIntegerField(db_column='Tékktími')  # Field name made lowercase.
    mismunatími = models.CharField(db_column='Mismunatími', max_length=15)  # Field name made lowercase.
    lesinn_tími = models.CharField(db_column='Lesinn tími', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lesnar_klst = models.IntegerField(db_column='Lesnar Klst')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lesnar_mín = models.IntegerField(db_column='Lesnar Mín')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lesnar_sek = models.IntegerField(db_column='Lesnar Sek')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lesin_sekbrot = models.IntegerField(db_column='Lesin Sekbrot')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þegar_færður_á_hlaupara = models.SmallIntegerField(db_column='Þegar færður á hlaupara')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fært_á_tímabókarlínu_nr_field = models.IntegerField(db_column='Fært á tímabókarlínu nr_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'Athl$Innlesnir tímar frá klukku'
        unique_together = (('mót_götuhlaup', 'lína'), ('mót_götuhlaup', 'tími', 'lína'),)


class AthlJobSchedulerAllowedJobsX(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    object_type = models.IntegerField(db_column='Object Type', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Job Scheduler Allowed Jobs x'
        unique_together = (('object_type', 'id'),)


class AthlJobSchedulerJobsX(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    job_no_field = models.IntegerField(db_column='Job No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    job_type = models.IntegerField(db_column='Job Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_id = models.IntegerField(db_column='Object ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    requested_start_date = models.DateTimeField(db_column='Requested Start Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    requested_start_time = models.DateTimeField(db_column='Requested Start Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    recurring_days = models.CharField(db_column='Recurring Days', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    recurring_minutes = models.DecimalField(db_column='Recurring Minutes', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exclude_mondays = models.SmallIntegerField(db_column='Exclude Mondays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exclude_tuesdays = models.SmallIntegerField(db_column='Exclude Tuesdays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exclude_wednesdays = models.SmallIntegerField(db_column='Exclude Wednesdays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exclude_thursdays = models.SmallIntegerField(db_column='Exclude Thursdays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exclude_fridays = models.SmallIntegerField(db_column='Exclude Fridays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exclude_saturdays = models.SmallIntegerField(db_column='Exclude Saturdays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exclude_sundays = models.SmallIntegerField(db_column='Exclude Sundays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_run_time_of_the_day = models.DateTimeField(db_column='First Run Time of the Day')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_run_time_of_the_day = models.DateTimeField(db_column='Last Run Time of the Day')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_run_date = models.DateTimeField(db_column='Last Run Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_start_date = models.DateTimeField(db_column='Run Start Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_start_time = models.DateTimeField(db_column='Run Start Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_end_date = models.DateTimeField(db_column='Run End Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_end_time = models.DateTimeField(db_column='Run End Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    printer = models.CharField(db_column='Printer', max_length=30)  # Field name made lowercase.
    print_to_file_printer = models.CharField(db_column='Print to File Printer', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    created_by_user_id = models.CharField(db_column='Created By User ID', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    creation_date = models.DateTimeField(db_column='Creation Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    creation_time = models.DateTimeField(db_column='Creation Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_after_job = models.IntegerField(db_column='Run After Job')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copied_from_job = models.IntegerField(db_column='Copied From Job')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    error_screen_exists = models.SmallIntegerField(db_column='Error Screen Exists')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    error_message = models.CharField(db_column='Error Message', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    backup_file_name = models.CharField(db_column='Backup File Name', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    overwrite_old_backup = models.SmallIntegerField(db_column='Overwrite old Backup')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    zup_file = models.BinaryField(db_column='ZUP File', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    session_id = models.IntegerField(db_column='Session ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Job Scheduler Jobs x'
        unique_together = (('status', 'requested_start_date', 'requested_start_time', 'priority', 'job_no_field'),)


class AthlJobSchedulerOptimiseTablesx(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    job_no_field = models.IntegerField(db_column='Job No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    company = models.CharField(db_column='Company', max_length=30)  # Field name made lowercase.
    table_no_field = models.IntegerField(db_column='Table No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'Athl$Job Scheduler Optimise Tablesx'
        unique_together = (('job_no_field', 'company', 'table_no_field'),)


class AthlJobSchedulerSetupX(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    key = models.CharField(db_column='Key', primary_key=True, max_length=1)  # Field name made lowercase.
    queue_sleep_time_in_minutes = models.DecimalField(db_column='Queue Sleep Time in minutes', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    queue_sleeping_from = models.DateTimeField(db_column='Queue Sleeping from')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    queue_sleeping_to = models.DateTimeField(db_column='Queue Sleeping to')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    work_directory = models.CharField(db_column='Work Directory', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    scheduler_running = models.SmallIntegerField(db_column='Scheduler Running')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    scheduler_user_id = models.CharField(db_column='Scheduler User ID', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    session_no_field = models.IntegerField(db_column='Session No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    start_date_of_scheduler = models.DateTimeField(db_column='Start Date of Scheduler')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    start_time_of_scheduler = models.DateTimeField(db_column='Start Time of Scheduler')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    default_start_time_of_jobs = models.DateTimeField(db_column='Default Start Time of Jobs')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    clean_zup_file = models.BinaryField(db_column='Clean ZUP File', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    log_on_for_scheduler = models.CharField(db_column='Log on For Scheduler', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    password_for_scheduler = models.CharField(db_column='Password for Scheduler', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Job Scheduler Setup x'


class AthlKeppenduridegaXml(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    primary_key = models.AutoField(db_column='Primary_Key', primary_key=True)  # Field name made lowercase.
    user_nationality = models.CharField(db_column='USER_NATIONALITY', max_length=30)  # Field name made lowercase.
    ic_gender_id = models.CharField(db_column='IC_GENDER_ID', max_length=30)  # Field name made lowercase.
    date_of_birth = models.CharField(db_column='DATE_OF_BIRTH', max_length=30)  # Field name made lowercase.
    personal_id = models.CharField(db_column='PERSONAL_ID', max_length=30)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=50)  # Field name made lowercase.
    middle_name = models.CharField(db_column='MIDDLE_NAME', max_length=50)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=50)  # Field name made lowercase.
    display_name = models.CharField(db_column='DISPLAY_NAME', max_length=50)  # Field name made lowercase.
    hlaup_ic_name = models.CharField(db_column='Hlaup_IC_NAME', max_length=30)  # Field name made lowercase.
    ár_haups_name = models.CharField(db_column='Ár_haups_NAME', max_length=30)  # Field name made lowercase.
    vegalengd_name = models.CharField(db_column='Vegalengd_NAME', max_length=30)  # Field name made lowercase.
    hópur_einstakslings = models.CharField(db_column='Hópur_einstakslings', max_length=80)  # Field name made lowercase.
    run_time = models.CharField(db_column='RUN_TIME', max_length=30)  # Field name made lowercase.
    chip_time = models.CharField(db_column='CHIP_TIME', max_length=30)  # Field name made lowercase.
    ic_user_id = models.CharField(db_column='IC_USER_ID', max_length=30)  # Field name made lowercase.
    participant_number = models.CharField(db_column='PARTICIPANT_NUMBER', max_length=30)  # Field name made lowercase.
    run_chip_number = models.CharField(db_column='RUN_CHIP_NUMBER', max_length=30)  # Field name made lowercase.
    run_tshirt_size = models.CharField(db_column='RUN_TSHIRT_SIZE', max_length=30)  # Field name made lowercase.
    run_group_name = models.CharField(db_column='RUN_GROUP_NAME', max_length=80)  # Field name made lowercase.
    run_best_time = models.CharField(db_column='RUN_BEST_TIME', max_length=20)  # Field name made lowercase.
    run_goal_time = models.CharField(db_column='RUN_GOAL_TIME', max_length=30)  # Field name made lowercase.
    run_chip_ownership_status = models.CharField(db_column='RUN_CHIP_OWNERSHIP_STATUS', max_length=30)  # Field name made lowercase.
    pay_method = models.CharField(db_column='PAY_METHOD', max_length=30)  # Field name made lowercase.
    payed_amount = models.CharField(db_column='PAYED_AMOUNT', max_length=30)  # Field name made lowercase.
    run_chip_bunch_number = models.CharField(db_column='RUN_CHIP_BUNCH_NUMBER', max_length=30)  # Field name made lowercase.
    ic_country_id = models.CharField(max_length=30)
    country_iso = models.CharField(max_length=50)
    eiginflaga = models.CharField(db_column='EiginFlaga', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$KeppendurIDEGA_XML'


class AthlKeppnisflokkarHlaups(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót_götuhlaup = models.CharField(db_column='Mót _ Götuhlaup', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    númer_flokks = models.IntegerField(db_column='Númer flokks')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_flokks = models.CharField(db_column='Heiti Flokks', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    aldur_frá = models.IntegerField(db_column='Aldur frá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_til = models.IntegerField(db_column='Aldur til')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_á_lista = models.CharField(db_column='Heiti á lista', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_á_skjali = models.CharField(db_column='Heiti á skjali', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skráningargjald = models.DecimalField(db_column='Skráningargjald', max_digits=38, decimal_places=20)  # Field name made lowercase.
    númer_í_töflu_rmar = models.IntegerField(db_column='Númer í töflu RMAR')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_flokks_fyrir_idega = models.CharField(db_column='Heiti flokks fyrir Idega', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enskt_heiti_á_skjali = models.CharField(db_column='Enskt heiti á skjali', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Keppnisflokkar hlaups'
        unique_together = (('mót_götuhlaup', 'númer_flokks'),)


class AthlKeppnisnmerMtsHlaups(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót_hlaup = models.CharField(db_column='Mót _ hlaup', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer = models.IntegerField(db_column='Rásnúmer')  # Field name made lowercase.
    keppendanúmer = models.CharField(db_column='Keppendanúmer', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Keppnisnúmer móts _ hlaups'
        unique_together = (('mót_hlaup', 'rásnúmer'),)


class AthlLinksToPhotoAlbums(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    competition_code = models.CharField(db_column='Competition Code', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    link_to_photo_album = models.CharField(db_column='Link to Photo Album', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    descripton = models.CharField(db_column='Descripton', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Links to Photo Albums'
        unique_together = (('competition_code', 'line_no_field'),)


class AthlLnd(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    tákn = models.CharField(db_column='Tákn', primary_key=True, max_length=10)  # Field name made lowercase.
    heiti = models.CharField(db_column='Heiti', max_length=50)  # Field name made lowercase.
    enskt_heiti = models.CharField(db_column='Enskt heiti', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    iso_skammstöfun = models.CharField(db_column='ISO Skammstöfun', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þjóðerni = models.CharField(db_column='Þjóðerni', max_length=30)  # Field name made lowercase.
    þjóðerni_enska_field = models.CharField(db_column='Þjóðerni (enska)', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'Athl$Lönd'
        unique_together = (('heiti', 'tákn'), ('iso_skammstöfun', 'tákn'), ('enskt_heiti', 'tákn'), ('þjóðerni_enska_field', 'tákn'), ('þjóðerni', 'tákn'),)


class AthlMenuSuiteMlCaption(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=50)  # Field name made lowercase.
    node_type = models.IntegerField(db_column='Node Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    language_code = models.CharField(db_column='Language Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    captionml_line_no_field = models.IntegerField(db_column='CaptionML Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    text = models.CharField(db_column='Text', max_length=100)  # Field name made lowercase.
    import_date = models.DateTimeField(db_column='Import Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    import_time = models.DateTimeField(db_column='Import Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Menu Suite ML Caption'
        unique_together = (('guid', 'node_type', 'line_no_field', 'language_code', 'captionml_line_no_field'), ('language_code', 'guid', 'node_type', 'line_no_field', 'captionml_line_no_field'),)


class AthlMenuSuiteNodes(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=50)  # Field name made lowercase.
    node_type = models.IntegerField(db_column='Node Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    firstchild = models.CharField(db_column='FirstChild', max_length=50)  # Field name made lowercase.
    parentnodeid = models.CharField(db_column='ParentNodeID', max_length=50)  # Field name made lowercase.
    image = models.IntegerField(db_column='Image')  # Field name made lowercase.
    isshortcut = models.SmallIntegerField(db_column='IsShortcut')  # Field name made lowercase.
    visible = models.SmallIntegerField(db_column='Visible')  # Field name made lowercase.
    enabled = models.SmallIntegerField(db_column='Enabled')  # Field name made lowercase.
    nextnodeid = models.CharField(db_column='NextNodeID', max_length=50)  # Field name made lowercase.
    memberofmenu = models.CharField(db_column='MemberOfMenu', max_length=50)  # Field name made lowercase.
    runobjecttype = models.IntegerField(db_column='RunObjectType')  # Field name made lowercase.
    runobjectid = models.IntegerField(db_column='RunObjectID')  # Field name made lowercase.
    menusuiteid = models.IntegerField(db_column='MenuSuiteID')  # Field name made lowercase.
    menusuitename = models.CharField(db_column='MenuSuiteName', max_length=50)  # Field name made lowercase.
    object_date = models.DateTimeField(db_column='Object Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_time = models.DateTimeField(db_column='Object Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_modified = models.SmallIntegerField(db_column='Object Modified')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version_list = models.CharField(db_column='Version List', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deleted = models.SmallIntegerField(db_column='Deleted')  # Field name made lowercase.
    import_date = models.DateTimeField(db_column='Import Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    import_time = models.DateTimeField(db_column='Import Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    input_line_no_field = models.IntegerField(db_column='Input Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    indentation = models.IntegerField(db_column='Indentation')  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort Order')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    expansion_status = models.SmallIntegerField(db_column='Expansion Status')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    departmentcategory = models.CharField(db_column='DepartmentCategory', max_length=30)  # Field name made lowercase.
    isdepartmentpage = models.SmallIntegerField(db_column='IsDepartmentPage')  # Field name made lowercase.
    visibleindesign = models.SmallIntegerField(db_column='VisibleInDesign')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Menu Suite Nodes'
        unique_together = (('guid', 'node_type', 'line_no_field'), ('sort_order', 'guid', 'node_type', 'line_no_field'), ('firstchild', 'guid', 'node_type', 'line_no_field'), ('nextnodeid', 'guid', 'node_type', 'line_no_field'),)


class AthlMenusuiteNode(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    node_id = models.CharField(db_column='Node ID', primary_key=True, max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    node_type = models.IntegerField(db_column='Node Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=80)  # Field name made lowercase.
    member_of_menu = models.CharField(db_column='Member of Menu', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_type = models.IntegerField(db_column='Object Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_id = models.IntegerField(db_column='Object ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parent_node_id = models.CharField(db_column='Parent Node ID', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    visible = models.SmallIntegerField(db_column='Visible')  # Field name made lowercase.
    enabled = models.SmallIntegerField(db_column='Enabled')  # Field name made lowercase.
    next_node_id = models.CharField(db_column='Next Node ID', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_child_id = models.CharField(db_column='First Child ID', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    image = models.IntegerField(db_column='Image')  # Field name made lowercase.
    is_shortcut = models.SmallIntegerField(db_column='Is Shortcut')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deleted = models.SmallIntegerField(db_column='Deleted')  # Field name made lowercase.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.
    menusuite_id = models.IntegerField(db_column='MenuSuite ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_menusuite_id = models.IntegerField(db_column='Last MenuSuite ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    show_node = models.SmallIntegerField(db_column='Show Node')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    scion_id = models.CharField(db_column='Scion ID', max_length=25)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    scions_filter = models.CharField(db_column='Scions Filter', max_length=25)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$MenuSuite Node'
        unique_together = (('object_type', 'object_id', 'node_id'), ('line_no_field', 'node_id'), ('scion_id', 'node_id'),)


class AthlMenusuiteNodeCaption(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    node_id = models.CharField(db_column='Node ID', primary_key=True, max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    language_id = models.IntegerField(db_column='Language ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    caption = models.CharField(db_column='Caption', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$MenuSuite Node Caption'
        unique_together = (('node_id', 'language_id'),)


class AthlMenusuiteNodeChanging(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entry_no_field = models.IntegerField(db_column='Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    node_id = models.CharField(db_column='Node ID', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    node_type = models.IntegerField(db_column='Node Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=80)  # Field name made lowercase.
    member_of_menu = models.CharField(db_column='Member of Menu', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_type = models.IntegerField(db_column='Object Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_id = models.IntegerField(db_column='Object ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parent_node_id = models.CharField(db_column='Parent Node ID', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    visible = models.SmallIntegerField(db_column='Visible')  # Field name made lowercase.
    enabled = models.SmallIntegerField(db_column='Enabled')  # Field name made lowercase.
    next_node_id = models.CharField(db_column='Next Node ID', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_child = models.CharField(db_column='First Child', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_shortcut = models.SmallIntegerField(db_column='Is Shortcut')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deleted = models.SmallIntegerField(db_column='Deleted')  # Field name made lowercase.
    menusuite_id = models.IntegerField(db_column='MenuSuite ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    language_id = models.IntegerField(db_column='Language ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    captionml = models.CharField(db_column='CaptionML', max_length=250)  # Field name made lowercase.
    menusuite_line_no_field = models.IntegerField(db_column='MenuSuite Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    xobjecttype = models.CharField(db_column='xObjectType', max_length=3)  # Field name made lowercase.
    xobject_id = models.CharField(db_column='xObject ID', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xvisible = models.CharField(db_column='xVisible', max_length=3)  # Field name made lowercase.
    xenabled = models.CharField(db_column='xEnabled', max_length=3)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=10)  # Field name made lowercase.
    xis_shortcut = models.CharField(db_column='xIs Shortcut', max_length=3)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xdeleted = models.CharField(db_column='xDeleted', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$MenuSuite Node Changing'
        unique_together = (('node_id', 'entry_no_field'), ('menusuite_id', 'menusuite_line_no_field', 'entry_no_field'),)


class AthlMenusuiteNodeLevelBuffer(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    level = models.IntegerField(db_column='Level', primary_key=True)  # Field name made lowercase.
    grow_id = models.CharField(db_column='Grow ID', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    scions_quantity = models.IntegerField(db_column='Scions Quantity')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$MenuSuite Node Level Buffer'


class AthlMetaskrFr(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    dagsetning_mets = models.DateTimeField(db_column='Dagsetning mets')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    árangur = models.CharField(db_column='Árangur', max_length=20)  # Field name made lowercase.
    árangur_raðsvæði = models.DecimalField(db_column='Árangur raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    staður_mets = models.CharField(db_column='Staður mets', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    methafi = models.CharField(db_column='Methafi', max_length=10)  # Field name made lowercase.
    heiti_methafa = models.CharField(db_column='Heiti methafa', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    félag_methafa = models.CharField(db_column='Félag methafa', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldursflokkur_frí = models.CharField(db_column='Aldursflokkur FRÍ', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    sería_eða_skipan_boðhlaupssv_field = models.CharField(db_column='Sería eða skipan boðhlaupssv_', max_length=150)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    röð_í_afrekaskrá = models.DecimalField(db_column='Röð í afrekaskrá', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fæðingarár_methafa = models.IntegerField(db_column='Fæðingarár methafa')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_methafa = models.IntegerField(db_column='Aldur methafa')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    óstaðfest = models.SmallIntegerField(db_column='Óstaðfest')  # Field name made lowercase.
    landssveit = models.SmallIntegerField(db_column='Landssveit')  # Field name made lowercase.
    línunr_í_afrekum = models.IntegerField(db_column='Línunr_ í afrekum')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vindur = models.DecimalField(db_column='Vindur', max_digits=38, decimal_places=20)  # Field name made lowercase.
    virkt = models.SmallIntegerField(db_column='Virkt')  # Field name made lowercase.
    athugasemd = models.CharField(db_column='Athugasemd', max_length=30)  # Field name made lowercase.
    athugasemd_ensk = models.CharField(db_column='Athugasemd Ensk', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skráningarnúmer_mets = models.IntegerField(db_column='Skráningarnúmer mets')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_vind = models.SmallIntegerField(db_column='Vantar vind')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_dag_og_mánuð = models.SmallIntegerField(db_column='Vantar dag og mánuð')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röðun_eftir_aldri = models.IntegerField(db_column='Röðun eftir aldri')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    innra_raðsvæði_1 = models.IntegerField(db_column='Innra raðsvæði 1')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    innra_raðsvæði_2 = models.IntegerField(db_column='Innra raðsvæði 2')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    innra_raðsvæði_3 = models.IntegerField(db_column='Innra raðsvæði 3')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    innra_heiti_aldursflokks = models.CharField(db_column='Innra heiti aldursflokks', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Metaskrá FRÍ'
        unique_together = (('úti_inni', 'aldursflokkur_frí', 'röð_í_afrekaskrá', 'lína'), ('grein', 'kyn', 'flokkur', 'úti_inni', 'aldursflokkur_frí', 'dagsetning_mets', 'lína'), ('grein', 'kyn', 'flokkur', 'úti_inni', 'aldursflokkur_frí', 'virkt', 'lína'), ('methafi', 'dagsetning_mets', 'lína'), ('grein', 'kyn', 'flokkur', 'úti_inni', 'röðun_eftir_aldri', 'lína'), ('innra_raðsvæði_1', 'innra_raðsvæði_2', 'heiti_methafa', 'innra_raðsvæði_3', 'röð_í_afrekaskrá', 'dagsetning_mets', 'lína'), ('röð_í_afrekaskrá', 'lína'), ('grein', 'kyn', 'flokkur', 'úti_inni', 'árangur_raðsvæði', 'lína'),)


class AthlMetaskrTil2010(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    land = models.CharField(db_column='Land', primary_key=True, max_length=10)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    dagsetning_mets = models.DateTimeField(db_column='Dagsetning mets')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=20)  # Field name made lowercase.
    árangur_raðsvæði = models.DecimalField(db_column='Árangur raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    staður_mets = models.CharField(db_column='Staður mets', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    methafi = models.CharField(db_column='Methafi', max_length=10)  # Field name made lowercase.
    heiti_methafa = models.CharField(db_column='Heiti methafa', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    félag_methafa = models.CharField(db_column='Félag methafa', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sería_eða_skipan_boðhlaupssv_field = models.CharField(db_column='Sería eða skipan boðhlaupssv_', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    röð_í_afrekaskrá = models.DecimalField(db_column='Röð í afrekaskrá', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kennitala_methafa = models.CharField(db_column='Kennitala methafa', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fæðingarár_methafa = models.IntegerField(db_column='Fæðingarár methafa')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_methafa = models.IntegerField(db_column='Aldur methafa')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    óstaðfest = models.SmallIntegerField(db_column='Óstaðfest')  # Field name made lowercase.
    innelsinn_árangur = models.CharField(db_column='Innelsinn árangur', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    landssveit = models.SmallIntegerField(db_column='Landssveit')  # Field name made lowercase.
    línunr_í_afrekum = models.IntegerField(db_column='Línunr_ í afrekum')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vindur = models.DecimalField(db_column='Vindur', max_digits=38, decimal_places=20)  # Field name made lowercase.
    virkt = models.SmallIntegerField(db_column='Virkt')  # Field name made lowercase.
    met_í_flokki = models.IntegerField(db_column='Met í flokki')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    línunúmer = models.IntegerField(db_column='Línunúmer')  # Field name made lowercase.
    athugasemd = models.CharField(db_column='Athugasemd', max_length=30)  # Field name made lowercase.
    athugasemd_ensk = models.CharField(db_column='Athugasemd Ensk', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skráningarnúmer_mets = models.IntegerField(db_column='Skráningarnúmer mets')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Metaskrá til 2010'
        unique_together = (('land', 'grein', 'kyn', 'flokkur', 'úti_inni', 'dagsetning_mets', 'lína'), ('grein', 'kyn', 'flokkur', 'land', 'dagsetning_mets', 'úti_inni', 'lína'), ('land', 'kyn', 'flokkur', 'röð_í_afrekaskrá', 'grein', 'úti_inni', 'dagsetning_mets', 'lína'), ('methafi', 'grein', 'flokkur', 'úti_inni', 'dagsetning_mets', 'land', 'kyn', 'lína'), ('úti_inni', 'met_í_flokki', 'röð_í_afrekaskrá', 'land', 'grein', 'kyn', 'flokkur', 'dagsetning_mets', 'lína'), ('methafi', 'dagsetning_mets', 'land', 'grein', 'kyn', 'flokkur', 'úti_inni', 'lína'), ('land', 'grein', 'kyn', 'flokkur', 'úti_inni', 'dagsetning_mets', 'árangur_raðsvæði', 'lína'), ('land', 'grein', 'kyn', 'flokkur', 'úti_inni', 'skráningarnúmer_mets', 'dagsetning_mets', 'lína'), ('land', 'úti_inni', 'met_í_flokki', 'grein', 'flokkur', 'dagsetning_mets', 'kyn', 'lína'),)


class AthlMeMynd(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    númer_myndar = models.CharField(db_column='Númer myndar', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    númer_keppanda = models.CharField(db_column='Númer Keppanda', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nafn_keppanda = models.CharField(db_column='Nafn keppanda', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    félag_keppanda = models.CharField(db_column='Félag keppanda', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    númer_raðar = models.IntegerField(db_column='Númer raðar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lýsing_raðar = models.CharField(db_column='Lýsing raðar', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    staða = models.IntegerField(db_column='Staða')  # Field name made lowercase.
    staðs_lýsing_raðar = models.IntegerField(db_column='Staðs_ lýsing raðar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    með_tvípunkti = models.SmallIntegerField(db_column='Með tvípunkti')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    leitarnafn = models.CharField(db_column='Leitarnafn', max_length=50)  # Field name made lowercase.
    viðbótarskýring_á_nafni = models.CharField(db_column='Viðbótarskýring á nafni', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Með á mynd'
        unique_together = (('númer_myndar', 'lína'), ('númer_keppanda', 'númer_myndar', 'lína'), ('nafn_keppanda', 'númer_myndar', 'lína'),)


class AthlMismNafniKeppVjskr(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    kennitala = models.CharField(db_column='Kennitala', primary_key=True, max_length=11)  # Field name made lowercase.
    nafn_skv_keppendatöflu = models.CharField(db_column='Nafn skv_ Keppendatöflu', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nafn_skv_þjóðskrá = models.CharField(db_column='Nafn skv_ þjóðskrá', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    laga_nafn = models.SmallIntegerField(db_column='Laga nafn')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nafn_var_lagað_þann = models.DateTimeField(db_column='Nafn var lagað þann')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Mism_ á nafni í Kepp v Þjóðskr'
        unique_together = (('nafn_skv_keppendatöflu', 'kennitala'),)


class AthlMyndasafn(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    númer = models.CharField(db_column='Númer', primary_key=True, max_length=10)  # Field name made lowercase.
    mynd = models.BinaryField(db_column='Mynd', blank=True, null=True)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    völlur = models.CharField(db_column='Völlur', max_length=30)  # Field name made lowercase.
    keppni = models.CharField(db_column='Keppni', max_length=10)  # Field name made lowercase.
    lýsing = models.CharField(db_column='Lýsing', max_length=250)  # Field name made lowercase.
    rétt_dagsetning = models.SmallIntegerField(db_column='Rétt dagsetning')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    réttur_mánuður = models.SmallIntegerField(db_column='Réttur mánuður')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rétt_ár = models.SmallIntegerField(db_column='Rétt ár')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nafn_á_keppni = models.CharField(db_column='Nafn á keppni', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_á_thumbnail = models.CharField(db_column='Slóð á thumbnail', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_á_large = models.CharField(db_column='Slóð á Large', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_á_mynd = models.CharField(db_column='Slóð á mynd', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ljósmyndari = models.CharField(db_column='Ljósmyndari', max_length=30)  # Field name made lowercase.
    keppnisgrein = models.CharField(db_column='Keppnisgrein', max_length=50)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    númer_greinar = models.IntegerField(db_column='Númer greinar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mappa = models.CharField(db_column='Mappa', max_length=100)  # Field name made lowercase.
    röð_innan_keppni = models.IntegerField(db_column='Röð innan keppni')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Myndasafn'
        unique_together = (('slóð_á_mynd', 'númer'), ('keppni', 'röð_innan_keppni', 'númer'), ('keppni', 'númer'),)


class AthlMyndirMtsActive(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    competition_code = models.CharField(db_column='Competition Code', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pictures_active = models.SmallIntegerField(db_column='Pictures Active')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Myndir móts Active'


class AthlMvatn99(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    hlaup = models.CharField(db_column='Hlaup', max_length=30)  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    heimili = models.CharField(db_column='Heimili', max_length=30)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Mývatn 99'


class AthlNijar(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    tákn = models.CharField(db_column='Tákn', primary_key=True, max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    fæðingardagur = models.DateTimeField(db_column='Fæðingardagur')  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.
    stofntákn_level_1 = models.CharField(db_column='Stofntákn level 1', max_length=1)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stofntákn_level_2 = models.CharField(db_column='Stofntákn level 2', max_length=1)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stofntákn_level_3 = models.CharField(db_column='Stofntákn level 3', max_length=1)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stofntákn_level_4 = models.CharField(db_column='Stofntákn level 4', max_length=1)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stofntákn_level_5 = models.CharField(db_column='Stofntákn level 5', max_length=1)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stofntákn_level_6 = models.CharField(db_column='Stofntákn level 6', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_maka = models.CharField(db_column='Tákn maka', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dánardagsetning = models.DateTimeField(db_column='Dánardagsetning')  # Field name made lowercase.
    heimili = models.CharField(db_column='Heimili', max_length=30)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    barnsfaðir_móðir = models.SmallIntegerField(db_column='Barnsfaðir_móðir')  # Field name made lowercase.
    fjölskyldunúmer = models.CharField(db_column='Fjölskyldunúmer', max_length=11)  # Field name made lowercase.
    foreldri_maka = models.SmallIntegerField(db_column='Foreldri maka')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    giftingardagsetning = models.DateTimeField(db_column='Giftingardagsetning')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Niðjar'
        unique_together = (('lína', 'tákn'),)


class AthlNoSeries(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    code = models.CharField(db_column='Code', primary_key=True, max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.
    default_nos_field = models.SmallIntegerField(db_column='Default Nos_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    manual_nos_field = models.SmallIntegerField(db_column='Manual Nos_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    date_order = models.SmallIntegerField(db_column='Date Order')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$No_ Series'


class AthlNoSeriesLine(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    series_code = models.CharField(db_column='Series Code', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    starting_date = models.DateTimeField(db_column='Starting Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    starting_no_field = models.CharField(db_column='Starting No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ending_no_field = models.CharField(db_column='Ending No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    warning_no_field = models.CharField(db_column='Warning No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    increment_by_no_field = models.IntegerField(db_column='Increment-by No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    last_no_used = models.CharField(db_column='Last No_ Used', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    open = models.SmallIntegerField(db_column='Open')  # Field name made lowercase.
    last_date_used = models.DateTimeField(db_column='Last Date Used')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$No_ Series Line'
        unique_together = (('series_code', 'line_no_field'), ('series_code', 'starting_date', 'starting_no_field', 'line_no_field'), ('starting_no_field', 'series_code', 'line_no_field'),)


class AthlObjectComparisonBuffer(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    type = models.IntegerField(db_column='Type', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    description_file_1 = models.CharField(db_column='Description File 1', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version_list_file_1 = models.CharField(db_column='Version List File 1', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modified_date_file_1 = models.DateTimeField(db_column='Modified Date File 1')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modified_time_file_1 = models.DateTimeField(db_column='Modified Time File 1')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description_file_2 = models.CharField(db_column='Description File 2', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version_list_file_2 = models.CharField(db_column='Version List File 2', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modified_date_file_2 = models.DateTimeField(db_column='Modified Date File 2')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modified_time_file_2 = models.DateTimeField(db_column='Modified Time File 2')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    imported_by_file_1 = models.CharField(db_column='Imported By File 1', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    imported_by_file_2 = models.CharField(db_column='Imported By File 2', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Object Comparison Buffer'
        unique_together = (('type', 'id'),)


class AthlPlanningAssignment(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    item_no_field = models.CharField(db_column='Item No_', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    variant_code = models.CharField(db_column='Variant Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_code = models.CharField(db_column='Location Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    latest_date = models.DateTimeField(db_column='Latest Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inactive = models.SmallIntegerField(db_column='Inactive')  # Field name made lowercase.
    action_msg_response_planning = models.SmallIntegerField(db_column='Action Msg_ Response Planning')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_change_planning = models.SmallIntegerField(db_column='Net Change Planning')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Planning Assignment'
        unique_together = (('item_no_field', 'variant_code', 'location_code'),)


class AthlPostCode(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    code = models.CharField(db_column='Code', primary_key=True, max_length=20)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Post Code'


class AthlPreaction(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entry_no_field = models.IntegerField(db_column='Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    xtable_no_field = models.IntegerField(db_column='xTable No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    location_group_filter = models.CharField(db_column='Location Group Filter', max_length=21)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    action_type = models.IntegerField(db_column='Action type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    table_no_field = models.IntegerField(db_column='Table No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    key = models.CharField(db_column='Key', max_length=200)  # Field name made lowercase.
    link_down = models.SmallIntegerField(db_column='Link Down')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    user_id = models.CharField(db_column='User ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    batchid = models.CharField(db_column='BatchID', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Preaction'
        unique_together = (('table_no_field', 'entry_no_field', 'location_group_filter'), ('table_no_field', 'key', 'action_type', 'entry_no_field'), ('date', 'table_no_field', 'entry_no_field'),)


class AthlProductionBomHeader(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    no_field = models.CharField(db_column='No_', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed because it ended with '_'.
    description = models.CharField(db_column='Description', max_length=30)  # Field name made lowercase.
    description_2 = models.CharField(db_column='Description 2', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    search_name = models.CharField(db_column='Search Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unit_of_measure_code = models.CharField(db_column='Unit of Measure Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    low_level_code = models.IntegerField(db_column='Low-Level Code')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    creation_date = models.DateTimeField(db_column='Creation Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_date_modified = models.DateTimeField(db_column='Last Date Modified')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    version_nos_field = models.CharField(db_column='Version Nos_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    no_series = models.CharField(db_column='No_ Series', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Production BOM Header'
        unique_together = (('search_name', 'no_field'),)


class AthlProductionBomLine(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    production_bom_no_field = models.CharField(db_column='Production BOM No_', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    version_code = models.CharField(db_column='Version Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    no_field = models.CharField(db_column='No_', max_length=20)  # Field name made lowercase. Field renamed because it ended with '_'.
    description = models.CharField(db_column='Description', max_length=30)  # Field name made lowercase.
    unit_of_measure_code = models.CharField(db_column='Unit of Measure Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quantity = models.DecimalField(db_column='Quantity', max_digits=38, decimal_places=20)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=10)  # Field name made lowercase.
    position_2 = models.CharField(db_column='Position 2', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    position_3 = models.CharField(db_column='Position 3', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    production_lead_time = models.CharField(db_column='Production Lead Time', max_length=32)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    routing_link_code = models.CharField(db_column='Routing Link Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    scrap_field = models.DecimalField(db_column='Scrap %', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    variant_code = models.CharField(db_column='Variant Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    starting_date = models.DateTimeField(db_column='Starting Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ending_date = models.DateTimeField(db_column='Ending Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    length = models.DecimalField(db_column='Length', max_digits=38, decimal_places=20)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=38, decimal_places=20)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=38, decimal_places=20)  # Field name made lowercase.
    depth = models.DecimalField(db_column='Depth', max_digits=38, decimal_places=20)  # Field name made lowercase.
    calculation_formula = models.IntegerField(db_column='Calculation Formula')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quantity_per = models.DecimalField(db_column='Quantity per', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Production BOM Line'
        unique_together = (('production_bom_no_field', 'version_code', 'line_no_field'), ('type', 'no_field', 'production_bom_no_field', 'version_code', 'line_no_field'),)


class AthlPrufutaflaMellumFields(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    key = models.CharField(db_column='Key', primary_key=True, max_length=10)  # Field name made lowercase.
    integer_field = models.IntegerField(db_column='Integer field')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    text_field = models.CharField(db_column='Text field', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code_field = models.CharField(db_column='Code field', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_field = models.DecimalField(db_column='Decimal field', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    option_field = models.IntegerField(db_column='Option field')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    boolean_field = models.SmallIntegerField(db_column='Boolean field')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_field = models.DateTimeField(db_column='Date field')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    time_field = models.DateTimeField(db_column='Time field')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    binary_field = models.BinaryField(db_column='Binary field')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    blob_field_1 = models.BinaryField(db_column='Blob field 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    blob_field_2 = models.BinaryField(db_column='Blob field 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_formula_1 = models.CharField(db_column='Date Formula 1', max_length=32)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    biginteger_field = models.BigIntegerField(db_column='Biginteger field')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    duration_field = models.BigIntegerField(db_column='Duration field')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    guid_field = models.CharField(db_column='GUID field', max_length=36)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    recorid_field = models.BinaryField(db_column='RecorID field')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    datetime_field = models.DateTimeField(db_column='DateTime field')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Prufutafla með öllum fields'


class AthlRecordssetatcompetition(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entryno = models.IntegerField(db_column='EntryNo', primary_key=True)  # Field name made lowercase.
    competitioncode = models.CharField(db_column='CompetitionCode', max_length=10)  # Field name made lowercase.
    eventcode = models.CharField(db_column='EventCode', max_length=10)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender')  # Field name made lowercase.
    agegroupcode = models.CharField(db_column='AgeGroupCode', max_length=10)  # Field name made lowercase.
    outdoorsindoors = models.IntegerField(db_column='OutdoorsIndoors')  # Field name made lowercase.
    performance = models.CharField(db_column='Performance', max_length=20)  # Field name made lowercase.
    recordinagegroup = models.CharField(db_column='RecordinAgeGroup', max_length=10)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    competitorscode = models.CharField(db_column='CompetitorsCode', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    club = models.CharField(db_column='Club', max_length=10)  # Field name made lowercase.
    yearofbirth = models.IntegerField(db_column='YearOfBirth')  # Field name made lowercase.
    eventlineno = models.IntegerField(db_column='EventLineNo')  # Field name made lowercase.
    statisticalorder = models.DecimalField(db_column='StatisticalOrder', max_digits=38, decimal_places=20)  # Field name made lowercase.
    previousrecord = models.CharField(db_column='PreviousRecord', max_length=20)  # Field name made lowercase.
    previousrecorddate = models.DateTimeField(db_column='PreviousRecordDate')  # Field name made lowercase.
    previousrecordname = models.CharField(db_column='PreviousRecordName', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$RecordsSetAtCompetition'
        unique_together = (('competitioncode', 'eventlineno', 'entryno'), ('competitioncode', 'recordinagegroup', 'statisticalorder', 'entryno'),)


class AthlRetailSetup(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    key = models.CharField(db_column='Key', primary_key=True, max_length=10)  # Field name made lowercase.
    local_store_no_field = models.CharField(db_column='Local Store No_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ls_retail_in_use = models.SmallIntegerField(db_column='LS Retail in Use')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ean_license_no_field = models.CharField(db_column='EAN License No_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    def_vat_bus_post_gr_price_field = models.CharField(db_column='Def_ VAT Bus_ Post Gr_ (Price)', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    def_price_includes_vat = models.SmallIntegerField(db_column='Def_ Price Includes VAT')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    source_code = models.CharField(db_column='Source Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    error_log = models.CharField(db_column='Error Log', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stop_on_error = models.SmallIntegerField(db_column='Stop On Error')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    store_no_nos_field = models.CharField(db_column='Store No_ Nos_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    item_sales_statistics_on = models.IntegerField(db_column='Item Sales Statistics on')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pos_terminal_statistics = models.SmallIntegerField(db_column='POS Terminal Statistics')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    staff_statistics = models.SmallIntegerField(db_column='Staff Statistics')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    payment_statistics = models.SmallIntegerField(db_column='Payment Statistics')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_date_modified = models.DateTimeField(db_column='Last Date Modified')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    days_before_trans_archive = models.IntegerField(db_column='Days Before Trans_ Archive')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dimension_1_mandatory = models.SmallIntegerField(db_column='Dimension 1 Mandatory')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    only_two_dimensions = models.SmallIntegerField(db_column='Only Two Dimensions')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xnumber_of_retries = models.IntegerField(db_column='xNumber of Retries')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    default_price_group = models.CharField(db_column='Default Price Group', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    post_total_disc_field = models.SmallIntegerField(db_column='Post Total Disc_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    post_infocode_disc_field = models.SmallIntegerField(db_column='Post Infocode Disc_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    post_line_disc_field = models.SmallIntegerField(db_column='Post Line Disc_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    post_periodic_disc_field = models.SmallIntegerField(db_column='Post Periodic Disc_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    post_cust_disc_field = models.SmallIntegerField(db_column='Post Cust_ Disc_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    post_coupon_disc_field = models.SmallIntegerField(db_column='Post Coupon Disc_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    item_posting_date = models.IntegerField(db_column='Item Posting Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    default_customer_posting = models.IntegerField(db_column='Default Customer Posting')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    update_cost_amount = models.SmallIntegerField(db_column='Update Cost Amount')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_labels_for_neg_stock = models.SmallIntegerField(db_column='Item Labels for Neg_ Stock')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_labels_on_price_change = models.SmallIntegerField(db_column='Item Labels on Price Change')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    post_always_reserve_items = models.SmallIntegerField(db_column='Post Always Reserve Items')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delete_printed_labels = models.SmallIntegerField(db_column='Delete Printed  Labels')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    difference_lcy_field = models.DecimalField(db_column='Difference (LCY)', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    difference_field = models.DecimalField(db_column='Difference (%)', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sale_compare_active = models.SmallIntegerField(db_column='Sale Compare Active')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sale_compare_date_value = models.CharField(db_column='Sale Compare Date Value', max_length=32)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xvariant_subfix_sequence_no_field = models.CharField(db_column='xVariant Subfix_Sequence no_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    autocreate_barcodes = models.IntegerField(db_column='Autocreate Barcodes')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    create_items_no_series = models.CharField(db_column='Create Items No_ Series', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_3rd_party_pos = models.SmallIntegerField(db_column='3rd Party POS')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    default_item_hierarchy = models.CharField(db_column='Default Item Hierarchy', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distribution_location = models.CharField(db_column='Distribution Location', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    def_store_hierarchy = models.CharField(db_column='Def_ Store Hierarchy', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inifile_section_identifier = models.IntegerField(db_column='IniFile Section Identifier')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    inifile_path = models.CharField(db_column='IniFile Path', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    barcode_lookup_in_sales_line = models.IntegerField(db_column='Barcode Lookup in Sales Line')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    default_subgroup_name = models.CharField(db_column='Default Subgroup Name', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allow_rename = models.SmallIntegerField(db_column='Allow Rename')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    default_logo = models.BinaryField(db_column='Default Logo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ls_retail_logo = models.BinaryField(db_column='LS Retail Logo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    po_version_no_markings = models.IntegerField(db_column='PO Version No_ Markings')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    register_card_information = models.SmallIntegerField(db_column='Register Card Information')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    autom_statistics_update = models.SmallIntegerField(db_column='Autom_ Statistics Update')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    update_store_price_info = models.SmallIntegerField(db_column='Update Store Price Info')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    include_special_groups = models.SmallIntegerField(db_column='Include Special Groups')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Retail Setup'


class AthlRetailUser(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    id = models.CharField(db_column='ID', primary_key=True, max_length=20)  # Field name made lowercase.
    main_menu_id = models.IntegerField(db_column='Main Menu ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    main_menu_delay_ms_field = models.IntegerField(db_column='Main Menu Delay (ms)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    store_no_field = models.CharField(db_column='Store No_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    till_group_code = models.CharField(db_column='Till Group Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    change_marked_today = models.SmallIntegerField(db_column='Change Marked Today')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    location_code = models.CharField(db_column='Location Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    e_mail_address = models.CharField(db_column='E-mail Address', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    view_inv_reason_codes = models.IntegerField(db_column='View Inv_ Reason Codes')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    view_inv_units = models.IntegerField(db_column='View Inv_ Units')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    view_inv_locations = models.IntegerField(db_column='View Inv_ Locations')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_is_rf_server_user = models.SmallIntegerField(db_column='User is RF Server User')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pos_super_user = models.SmallIntegerField(db_column='POS Super User')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emphasize_info_values = models.SmallIntegerField(db_column='Emphasize Info Values')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buyer_group_code = models.CharField(db_column='Buyer Group Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_logs_on_automatically = models.SmallIntegerField(db_column='User Logs on Automatically')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Retail User'


class AthlRichTextFormatCodes(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    number = models.IntegerField(db_column='Number', primary_key=True)  # Field name made lowercase.
    printer_code_name = models.CharField(db_column='Printer Code Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    begin_code = models.CharField(db_column='Begin Code', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_code = models.CharField(db_column='End Code', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comments = models.CharField(db_column='Comments', max_length=50)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Rich Text Format Codes'
        unique_together = (('printer_code_name', 'number'), ('type', 'number'),)


class AthlSchedulerJobHeader(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    job_id = models.CharField(db_column='Job ID', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(db_column='Description', max_length=30)  # Field name made lowercase.
    from_location_code = models.CharField(db_column='From-Location Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    use_current_location = models.SmallIntegerField(db_column='Use Current Location')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_date_checked = models.DateTimeField(db_column='Last Date Checked')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_time_checked = models.DateTimeField(db_column='Last Time Checked')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    time_between_check = models.IntegerField(db_column='Time Between Check')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    time_units = models.IntegerField(db_column='Time Units')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    next_check_date = models.DateTimeField(db_column='Next Check Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    next_check_time = models.DateTimeField(db_column='Next Check Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_status = models.IntegerField(db_column='Run Status')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    error_handling = models.IntegerField(db_column='Error Handling')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    error_occurred = models.SmallIntegerField(db_column='Error Occurred')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    valid_on_sundays = models.SmallIntegerField(db_column='Valid on Sundays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    valid_on_mondays = models.SmallIntegerField(db_column='Valid on Mondays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    valid_on_tuesdays = models.SmallIntegerField(db_column='Valid on Tuesdays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    valid_on_wednesdays = models.SmallIntegerField(db_column='Valid on Wednesdays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    valid_on_thursdays = models.SmallIntegerField(db_column='Valid on Thursdays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    valid_on_fridays = models.SmallIntegerField(db_column='Valid on Fridays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    valid_on_saturdays = models.SmallIntegerField(db_column='Valid on Saturdays')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    starting_time = models.DateTimeField(db_column='Starting Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ending_time = models.DateTimeField(db_column='Ending Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_type = models.IntegerField(db_column='Object Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_no_field = models.IntegerField(db_column='Object No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    object_name = models.CharField(db_column='Object Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uses_scheduler_job_record = models.SmallIntegerField(db_column='Uses Scheduler Job Record')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_message_text = models.CharField(db_column='Last Message Text', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_log_entry = models.IntegerField(db_column='Last Log Entry')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    scheduler_job_type_code = models.CharField(db_column='Scheduler Job Type Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subjobs_defined_by_job = models.CharField(db_column='Subjobs Defined by Job', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distribution_restrictions = models.IntegerField(db_column='Distribution Restrictions')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    include_exclude_list_exists = models.SmallIntegerField(db_column='Include_Exclude List Exists')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distribution_sublocations = models.IntegerField(db_column='Distribution Sublocations')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    retry_log_entry = models.IntegerField(db_column='Retry Log Entry')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    run_for_location = models.CharField(db_column='Run For Location', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    retry_counter = models.IntegerField(db_column='Retry Counter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nasid = models.CharField(db_column='NASID', max_length=20)  # Field name made lowercase.
    use_job_id = models.CharField(db_column='Use Job ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_batch_id = models.CharField(db_column='Last Batch ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    text = models.CharField(db_column='Text', max_length=250)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    integer = models.IntegerField(db_column='Integer')  # Field name made lowercase.
    decimal = models.DecimalField(db_column='Decimal', max_digits=38, decimal_places=20)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    option = models.IntegerField(db_column='Option')  # Field name made lowercase.
    boolean = models.SmallIntegerField(db_column='Boolean')  # Field name made lowercase.
    job_type = models.IntegerField(db_column='Job Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    calcdate_formula = models.CharField(db_column='Calcdate Formula', max_length=32)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_duration = models.BigIntegerField(db_column='Last Duration')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_starting_date_and_time = models.DateTimeField(db_column='Last Starting Date and Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_ending_date_and_time = models.DateTimeField(db_column='Last Ending Date and Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_no_of_seconds = models.DecimalField(db_column='Last no_ of Seconds', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Scheduler Job Header'
        unique_together = (('next_check_date', 'next_check_time', 'scheduler_job_type_code', 'job_id'), ('subjobs_defined_by_job', 'job_id'),)


class AthlSchedulerJobLine(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    scheduler_job_id = models.CharField(db_column='Scheduler Job ID', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subjob_id = models.CharField(db_column='Subjob ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lock_seq_field = models.IntegerField(db_column='Lock Seq_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    enabled = models.SmallIntegerField(db_column='Enabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Scheduler Job Line'
        unique_together = (('scheduler_job_id', 'subjob_id'), ('subjob_id', 'scheduler_job_id'), ('scheduler_job_id', 'lock_seq_field', 'subjob_id'),)


class AthlSchedulerJobType(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    type_code = models.CharField(db_column='Type Code', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(db_column='Description', max_length=30)  # Field name made lowercase.
    object_type = models.IntegerField(db_column='Object Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_no_field = models.IntegerField(db_column='Object No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    object_name = models.CharField(db_column='Object Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distribution_restrictions = models.IntegerField(db_column='Distribution Restrictions')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Scheduler Job Type'


class AthlSchedulerLog(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entry_no_field = models.IntegerField(db_column='Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    scheduler_job_id = models.CharField(db_column='Scheduler Job ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    error_occured = models.SmallIntegerField(db_column='Error Occured')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    starting_date = models.DateTimeField(db_column='Starting Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    starting_time = models.DateTimeField(db_column='Starting Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ending_date = models.DateTimeField(db_column='Ending Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ending_time = models.DateTimeField(db_column='Ending Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    message_text = models.CharField(db_column='Message Text', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    retry_log_no_field = models.IntegerField(db_column='Retry Log No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    first_package_no_field = models.IntegerField(db_column='First Package No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    last_package_no_field = models.IntegerField(db_column='Last Package No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    batch_id = models.CharField(db_column='Batch ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Scheduler Log'
        unique_together = (('scheduler_job_id', 'entry_no_field'), ('starting_date', 'starting_time', 'entry_no_field'),)


class AthlSchedulerLogLine(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entry_no_field = models.IntegerField(db_column='Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    subjob_id = models.CharField(db_column='Subjob ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_source_counter = models.IntegerField(db_column='First Source Counter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_source_counter = models.IntegerField(db_column='Last Source Counter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    no_of_runs = models.IntegerField(db_column='No_ of Runs')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Scheduler Log Line'
        unique_together = (('entry_no_field', 'line_no_field'), ('subjob_id', 'entry_no_field', 'line_no_field'),)


class AthlSchedulerReplicationCounter(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    scheduler_job_id = models.CharField(db_column='Scheduler Job ID', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subjob_id = models.CharField(db_column='Subjob ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_source_counter = models.IntegerField(db_column='Last Source Counter')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Scheduler Replication Counter'
        unique_together = (('scheduler_job_id', 'subjob_id'),)


class AthlSchedulerSetup(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    scheduler_sleep_sec_field = models.IntegerField(db_column='Scheduler Sleep Sec_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    scheduler_shut_down_date = models.DateTimeField(db_column='Scheduler Shut Down Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    scheduler_shut_down_time = models.DateTimeField(db_column='Scheduler Shut Down Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    scheduler_is_running = models.SmallIntegerField(db_column='Scheduler is Running')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_date_modified = models.DateTimeField(db_column='Last Date Modified')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    default_distr_chg_mess_field = models.SmallIntegerField(db_column='Default Distr_ Chg_ Mess_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    days_actions_exist = models.IntegerField(db_column='Days Actions Exist')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    days_sched_log_exists = models.IntegerField(db_column='Days Sched_ Log Exists')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    days_inc_outg_msg_exists = models.IntegerField(db_column='Days Inc__Outg_ Msg_ Exists')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    days_preaction_log_exists = models.IntegerField(db_column='Days Preaction Log Exists')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    replicate_using_preactions = models.SmallIntegerField(db_column='Replicate using Preactions')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enable_nas_scheduler = models.SmallIntegerField(db_column='Enable NAS Scheduler')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_of_retries = models.IntegerField(db_column='Number of Retries')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    minutes_between_tries = models.IntegerField(db_column='Minutes Between Tries')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_repl_nos_field = models.CharField(db_column='Object Repl_ Nos_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    statment_post_repl_job = models.CharField(db_column='Statment Post Repl_ Job', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_repl_subjob = models.CharField(db_column='Object Repl_ Subjob', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    loc_group_filter_delimiter = models.CharField(db_column='Loc_ Group Filter Delimiter', max_length=1)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    replicate_using_register_entry = models.SmallIntegerField(db_column='Replicate using Register Entry')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fob_export_path = models.CharField(db_column='FOB Export Path', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    path_for_fob_backup = models.CharField(db_column='Path for FOB Backup', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fob_file_prefix = models.CharField(db_column='FOB File Prefix', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fob_file_nos_field = models.CharField(db_column='FOB File Nos_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    replicate_fob_files = models.SmallIntegerField(db_column='Replicate FOB Files')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Scheduler Setup'


class AthlSchedulerSubjob(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    id = models.CharField(db_column='ID', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.
    replication_method = models.IntegerField(db_column='Replication Method')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    what_to_do = models.IntegerField(db_column='What To Do')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_transfer_type = models.IntegerField(db_column='Field Transfer Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enabled = models.SmallIntegerField(db_column='Enabled')  # Field name made lowercase.
    from_location_design = models.CharField(db_column='From-Location Design', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    to_location_design = models.CharField(db_column='To-Location Design', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    action_table_id = models.IntegerField(db_column='Action Table ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    from_table_id = models.IntegerField(db_column='From-Table ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    move_actions = models.SmallIntegerField(db_column='Move Actions')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    replication_counter = models.IntegerField(db_column='Replication Counter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    to_table_id = models.IntegerField(db_column='To-Table ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    from_to_table_filters_exist = models.SmallIntegerField(db_column='From_To Table Filters Exist')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transfer_field_list_exists = models.SmallIntegerField(db_column='Transfer Field List Exists')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    update_replication_counter = models.SmallIntegerField(db_column='Update Replication Counter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mark_sent_records = models.IntegerField(db_column='Mark sent records')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    linked_table_exists = models.SmallIntegerField(db_column='Linked Table Exists')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    repl_counter_interval = models.IntegerField(db_column='Repl_ Counter Interval')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    include_flowfields = models.SmallIntegerField(db_column='Include FlowFields')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    upd_counter_on_empty_interval = models.SmallIntegerField(db_column='Upd_ Counter on Empty Interval')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    action_counter_interval = models.IntegerField(db_column='Action Counter Interval')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    no_distribution_filter = models.SmallIntegerField(db_column='No Distribution Filter')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Scheduler Subjob'
        unique_together = (('replication_method', 'enabled', 'id'),)


class AthlSchedulerSubjobFieldList(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    subjob_id = models.CharField(db_column='Subjob ID', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    table_id = models.IntegerField(db_column='Table ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    from_field_no_field = models.IntegerField(db_column='From-Field No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    to_field_no_field = models.IntegerField(db_column='To-Field No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    primary_key = models.CharField(db_column='Primary Key', max_length=60)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    from_field_type = models.IntegerField(db_column='From-Field Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    conversion_type = models.IntegerField(db_column='Conversion Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    conversion_string = models.CharField(db_column='Conversion String', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_value = models.CharField(db_column='Field Value', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enabled = models.SmallIntegerField(db_column='Enabled')  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort Order')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Scheduler Subjob Field List'
        unique_together = (('subjob_id', 'table_id', 'from_field_no_field', 'to_field_no_field'), ('sort_order', 'subjob_id', 'table_id', 'from_field_no_field', 'to_field_no_field'),)


class AthlSchedulerSubjobFilter(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    subjob_id = models.CharField(db_column='Subjob ID', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    location_code = models.CharField(db_column='Location Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_no_field = models.IntegerField(db_column='Field No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_name = models.CharField(db_column='Field Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    value_1 = models.CharField(db_column='Value 1', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    value_2 = models.CharField(db_column='Value 2', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    filter_type = models.IntegerField(db_column='Filter Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    apply_filter_on = models.IntegerField(db_column='Apply Filter On')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    primary_key = models.CharField(db_column='Primary Key', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Scheduler Subjob Filter'
        unique_together = (('subjob_id', 'type', 'location_code', 'field_no_field'),)


class AthlSchedulerSubjobLinkedTable(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    subjob_id = models.CharField(db_column='Subjob ID', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    from_table_id = models.IntegerField(db_column='From-Table ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    to_table_id = models.IntegerField(db_column='To-Table ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_transfer_type = models.IntegerField(db_column='Field Transfer Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Scheduler Subjob Linked Table'
        unique_together = (('subjob_id', 'from_table_id'),)


class AthlSchedulerTimeSlot(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    code = models.CharField(db_column='Code', primary_key=True, max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Scheduler Time Slot'


class AthlSchedulerTimeSlotLine(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    time_slot_code = models.CharField(db_column='Time Slot Code', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    time_slot_line = models.IntegerField(db_column='Time Slot Line')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    start_time = models.DateTimeField(db_column='Start Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Scheduler Time Slot Line'
        unique_together = (('time_slot_code', 'time_slot_line'), ('start_time', 'time_slot_code', 'time_slot_line'),)


class AthlSkannaarFlgur(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    tölva = models.CharField(db_column='Tölva', primary_key=True, max_length=50)  # Field name made lowercase.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    númer_flögu = models.CharField(db_column='Númer flögu', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    innra_rásnúmer = models.IntegerField(db_column='Innra rásnúmer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nafn = models.CharField(db_column='Nafn', max_length=50)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    aldursflokkur = models.CharField(db_column='Aldursflokkur', max_length=30)  # Field name made lowercase.
    land = models.CharField(db_column='Land', max_length=10)  # Field name made lowercase.
    heiti_sveitar = models.CharField(db_column='Heiti sveitar', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nafn_ekki_komið = models.SmallIntegerField(db_column='Nafn ekki komið')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mótafilter = models.CharField(db_column='Mótafilter', max_length=100)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    tími = models.DateTimeField(db_column='Tími')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Skannaðar flögur'
        unique_together = (('tölva', 'lína'),)


class AthlSkipanBohlSvGtuhlaupi(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    hlaup = models.CharField(db_column='Hlaup', primary_key=True, max_length=10)  # Field name made lowercase.
    rásnúmer = models.IntegerField(db_column='Rásnúmer')  # Field name made lowercase.
    sprettur_númer = models.IntegerField(db_column='Sprettur númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kennitala = models.CharField(db_column='Kennitala', max_length=15)  # Field name made lowercase.
    keppendanúmer = models.CharField(db_column='Keppendanúmer', max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E-mail', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bolastærð = models.CharField(db_column='Bolastærð', max_length=15)  # Field name made lowercase.
    tími = models.CharField(db_column='Tími', max_length=10)  # Field name made lowercase.
    nafn_skv_þjóðskrá = models.CharField(db_column='Nafn skv_ Þjóðskrá', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skráður_í_spretti_nr_field = models.CharField(db_column='Skráður í spretti nr_', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    liðsnafn = models.CharField(db_column='Liðsnafn', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Skipan boðhl_sv í götuhlaupi'
        unique_together = (('hlaup', 'rásnúmer', 'sprettur_númer'),)


class AthlSkipanBohlaupssvSkrnbkln(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    bók = models.CharField(db_column='Bók', primary_key=True, max_length=10)  # Field name made lowercase.
    lína_í_bók = models.IntegerField(db_column='Lína í bók')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    sprettur_nr = models.IntegerField(db_column='Sprettur nr')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    leitarnafn = models.CharField(db_column='Leitarnafn', max_length=50)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Skipan boðhlaupssv Skránbóklín'
        unique_together = (('bók', 'lína_í_bók', 'lína'), ('bók', 'lína_í_bók', 'sprettur_nr', 'lína'),)


class AthlSkipanBohlaupssvAfrekum(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína_í_afrekum = models.IntegerField(db_column='Lína í Afrekum', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    sprettur_nr = models.IntegerField(db_column='Sprettur nr')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    leitarnafn = models.CharField(db_column='Leitarnafn', max_length=50)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Skipan boðhlaupssv í Afrekum'
        unique_together = (('lína_í_afrekum', 'lína'), ('lína_í_afrekum', 'sprettur_nr', 'lína'),)


class AthlSkipanBohlaupssveitar(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót = models.CharField(db_column='Mót', primary_key=True, max_length=10)  # Field name made lowercase.
    greinarnúmer = models.IntegerField(db_column='Greinarnúmer')  # Field name made lowercase.
    rásnúmer = models.IntegerField(db_column='Rásnúmer')  # Field name made lowercase.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    sprettur = models.IntegerField(db_column='Sprettur')  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    rásnúmer_keppanda = models.IntegerField(db_column='Rásnúmer keppanda')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nýtt_rásnúmer_tmp = models.IntegerField(db_column='Nýtt Rásnúmer TMP')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nýtt_rásnúmer_keppanda_tmp = models.IntegerField(db_column='Nýtt Rásnúmer keppanda TMP')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    nafn_keppanda = models.CharField(db_column='Nafn keppanda', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Skipan boðhlaupssveitar'
        unique_together = (('mót', 'greinarnúmer', 'rásnúmer', 'lína'), ('mót', 'rásnúmer', 'greinarnúmer', 'lína'), ('keppandanúmer', 'mót', 'greinarnúmer', 'rásnúmer', 'lína'), ('mót', 'rásnúmer_keppanda', 'greinarnúmer', 'rásnúmer', 'lína'),)


class AthlSkrningarbkAfreka(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    bók = models.CharField(db_column='Bók', primary_key=True, max_length=10)  # Field name made lowercase.
    heiti = models.CharField(db_column='Heiti', max_length=30)  # Field name made lowercase.
    tegund_greinar = models.IntegerField(db_column='Tegund greinar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tími_í_mínútum = models.DecimalField(db_column='Tími í mínútum', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    athleteregisteringachievem = models.CharField(db_column='AthleteRegisteringAchievem', max_length=50)  # Field name made lowercase.
    competitornumber = models.CharField(db_column='CompetitorNumber', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Skráningarbók afreka'


class AthlSkrningarbkarlnurAfreka(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    bók = models.CharField(db_column='Bók', primary_key=True, max_length=10)  # Field name made lowercase.
    línunúmer = models.IntegerField(db_column='Línunúmer')  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=10)  # Field name made lowercase.
    vindur = models.DecimalField(db_column='Vindur', max_digits=38, decimal_places=20)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    metrar = models.DecimalField(db_column='Metrar', max_digits=38, decimal_places=20)  # Field name made lowercase.
    tími = models.CharField(db_column='Tími', max_length=10)  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    löglegt = models.SmallIntegerField(db_column='Löglegt')  # Field name made lowercase.
    röð = models.CharField(db_column='Röð', max_length=10)  # Field name made lowercase.
    rafmagnstímataka = models.SmallIntegerField(db_column='Rafmagnstímataka')  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    aldur_keppanda = models.IntegerField(db_column='Aldur keppanda')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mót = models.CharField(db_column='Mót', max_length=10)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    heiti_móts = models.CharField(db_column='Heiti Móts', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sería = models.CharField(db_column='Sería', max_length=150)  # Field name made lowercase.
    athugasemd = models.CharField(db_column='Athugasemd', max_length=125)  # Field name made lowercase.
    riðill = models.IntegerField(db_column='Riðill')  # Field name made lowercase.
    vantar_vind = models.SmallIntegerField(db_column='Vantar vind')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    erlendur_ríkisborgari = models.SmallIntegerField(db_column='Erlendur ríkisborgari')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    riðill_númer = models.IntegerField(db_column='Riðill númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grein_númer = models.IntegerField(db_column='Grein númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    klst_field = models.IntegerField(db_column='Klst_')  # Field name made lowercase. Field renamed because it ended with '_'.
    mín_field = models.IntegerField(db_column='Mín_')  # Field name made lowercase. Field renamed because it ended with '_'.
    sek_field = models.IntegerField(db_column='Sek_')  # Field name made lowercase. Field renamed because it ended with '_'.
    brot = models.IntegerField(db_column='Brot')  # Field name made lowercase.
    leitarnafn = models.CharField(db_column='Leitarnafn', max_length=35)  # Field name made lowercase.
    félag_innan_sambands = models.CharField(db_column='Félag innan sambands', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_frá = models.IntegerField(db_column='Aldur frá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_til = models.IntegerField(db_column='Aldur til')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_á_úrslit_móts = models.CharField(db_column='Slóð á úrslit móts', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keppnisvöllur = models.CharField(db_column='Keppnisvöllur', max_length=50)  # Field name made lowercase.
    fél_í_boðhlaupi_eignarfall_field = models.CharField(db_column='Fél_ í boðhlaupi (eignarfall)', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wrkraðsvæði = models.DecimalField(db_column='WrkRaðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase.
    innlesinn_árangur = models.CharField(db_column='Innlesinn árangur', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vantar_dag_og_mánuð = models.SmallIntegerField(db_column='Vantar dag og mánuð')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    innlesið_fæðingarár = models.IntegerField(db_column='Innlesið fæðingarár')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bókstafur_boðhlaupssveitar = models.CharField(db_column='Bókstafur boðhlaupssveitar', max_length=1)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sleppa_aldurstakmörkunum = models.SmallIntegerField(db_column='Sleppa aldurstakmörkunum')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    innlesið_félag = models.CharField(db_column='Innlesið félag', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    handreiknuð_iaaf_stig = models.IntegerField(db_column='Handreiknuð IAAF stig')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Skráningarbókarlínur afreka'
        unique_together = (('bók', 'línunúmer'), ('keppandanúmer', 'bók', 'línunúmer'), ('bók', 'leitarnafn', 'grein', 'línunúmer'), ('bók', 'grein', 'kyn', 'flokkur', 'úti_inni', 'wrkraðsvæði', 'línunúmer'), ('bók', 'staður', 'dagsetning', 'línunúmer'),)


class AthlSkrirFyrirLokSkrningarfr(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    rásnúmer = models.IntegerField(db_column='Rásnúmer', primary_key=True)  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=50)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Skráðir fyrir lok skráningarfr'
        unique_together = (('kennitala', 'rásnúmer'),)


class AthlSkrslulog(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    tími = models.DateTimeField(db_column='Tími')  # Field name made lowercase.
    report_id = models.IntegerField(db_column='Report ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ár = models.IntegerField(db_column='Ár')  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Skýrslulog'


class AthlStandardText(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    code = models.CharField(db_column='Code', primary_key=True, max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Standard Text'


class AthlStaur(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    staður = models.CharField(db_column='Staður', primary_key=True, max_length=30)  # Field name made lowercase.
    enskt_heiti_staðar = models.CharField(db_column='Enskt heiti staðar', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    land = models.CharField(db_column='Land', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Staður'


class AthlStigakeppniInnslegin(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót = models.CharField(db_column='Mót', primary_key=True, max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    röð = models.IntegerField(db_column='Röð')  # Field name made lowercase.
    röð_texti = models.CharField(db_column='Röð - texti', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    stig = models.DecimalField(db_column='Stig', max_digits=38, decimal_places=20)  # Field name made lowercase.
    bókstafur_félags = models.CharField(db_column='Bókstafur félags', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_félags = models.CharField(db_column='Heiti félags', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Stigakeppni innslegin'
        unique_together = (('mót', 'kyn', 'röð'),)


class AthlStigataflaUnglingaFr(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.AutoField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    eventcode = models.CharField(db_column='EventCode', max_length=10)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender')  # Field name made lowercase.
    agegroup = models.CharField(db_column='AgeGroup', max_length=10)  # Field name made lowercase.
    outorindoors = models.IntegerField(db_column='OutOrIndoors')  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    validfrom = models.DateTimeField(db_column='ValidFrom')  # Field name made lowercase.
    refresultfor1000pts = models.CharField(db_column='RefResultFor1000Pts', max_length=10)  # Field name made lowercase.
    refresultfor1000ptsmeters = models.DecimalField(db_column='RefResultFor1000PtsMeters', max_digits=38, decimal_places=20)  # Field name made lowercase.
    refresultfor1000ptsseconds = models.DecimalField(db_column='RefResultFor1000PtsSeconds', max_digits=38, decimal_places=20)  # Field name made lowercase.
    refresultfor800pts = models.CharField(db_column='RefResultFor800Pts', max_length=10)  # Field name made lowercase.
    refresultfor800ptsmeters = models.DecimalField(db_column='RefResultFor800PtsMeters', max_digits=38, decimal_places=20)  # Field name made lowercase.
    refresultfor800ptsseconds = models.DecimalField(db_column='RefResultFor800PtsSeconds', max_digits=38, decimal_places=20)  # Field name made lowercase.
    noofafrekrecords = models.IntegerField(db_column='NoOfAfrekRecords')  # Field name made lowercase.
    refresultfor100pts = models.CharField(db_column='RefResultFor100Pts', max_length=10)  # Field name made lowercase.
    factor1forcentimeters = models.DecimalField(db_column='Factor1ForCentimeters', max_digits=38, decimal_places=20)  # Field name made lowercase.
    factor2forcentimeters = models.DecimalField(db_column='Factor2ForCentimeters', max_digits=38, decimal_places=20)  # Field name made lowercase.
    factor1forseconds = models.DecimalField(db_column='Factor1ForSeconds', max_digits=38, decimal_places=20)  # Field name made lowercase.
    factor2forseconds = models.DecimalField(db_column='Factor2ForSeconds', max_digits=38, decimal_places=20)  # Field name made lowercase.
    eventtype1track2field = models.IntegerField(db_column='EventType1Track2Field')  # Field name made lowercase.
    refresultfor100ptsmeters = models.DecimalField(db_column='RefResultFor100PtsMeters', max_digits=38, decimal_places=20)  # Field name made lowercase.
    refresultfor100ptsseconds = models.DecimalField(db_column='RefResultFor100PtsSeconds', max_digits=38, decimal_places=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Stigatafla Unglinga FRÍ'
        unique_together = (('lína', 'eventcode', 'gender', 'agegroup', 'outorindoors', 'age', 'validfrom'),)


class AthlStigataflaUnglinga(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    land = models.CharField(db_column='Land', primary_key=True, max_length=10)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    röð_í_afrekaskrá = models.IntegerField(db_column='Röð í afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    frádráttur = models.DecimalField(db_column='Frádráttur', max_digits=38, decimal_places=20)  # Field name made lowercase.
    number_18_ára = models.DecimalField(db_column='18 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_ára = models.DecimalField(db_column='17 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_16_ára = models.DecimalField(db_column='16 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15_ára = models.DecimalField(db_column='15 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_14_ára = models.DecimalField(db_column='14 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_13_ára = models.DecimalField(db_column='13 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_ára = models.DecimalField(db_column='12 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_11_ára = models.DecimalField(db_column='11 ára', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    frádráttur_2 = models.DecimalField(db_column='Frádráttur 2', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    árangur_2 = models.DecimalField(db_column='Árangur 2', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    frádráttur_3 = models.DecimalField(db_column='Frádráttur 3', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    árangur_3 = models.DecimalField(db_column='Árangur 3', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stig_f_árangur_í_línu_3 = models.SmallIntegerField(db_column='Stig f_ árangur í Línu 3')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Stigatafla unglinga'
        unique_together = (('land', 'grein', 'kyn', 'flokkur', 'úti_inni', 'lína'), ('röð_í_afrekaskrá', 'land', 'grein', 'kyn', 'flokkur', 'úti_inni', 'lína'), ('land', 'röð_í_afrekaskrá', 'grein', 'kyn', 'flokkur', 'úti_inni', 'lína'),)


class AthlStigatreiknFUnglingaraut(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    grein = models.CharField(db_column='Grein', primary_key=True, max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    aldur = models.IntegerField(db_column='Aldur')  # Field name made lowercase.
    svæði_a = models.DecimalField(db_column='Svæði A', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    svæði_b = models.DecimalField(db_column='Svæði B', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    svæði_c = models.DecimalField(db_column='Svæði C', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Stigaútreikn_ f_ unglingaþraut'
        unique_together = (('grein', 'kyn', 'flokkur', 'úti_inni', 'aldur'),)


class AthlStore(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    no_field = models.CharField(db_column='No_', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed because it ended with '_'.
    responsibility_center = models.CharField(db_column='Responsibility Center', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30)  # Field name made lowercase.
    address_2 = models.CharField(db_column='Address 2', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    city = models.CharField(db_column='City', max_length=30)  # Field name made lowercase.
    post_code = models.CharField(db_column='Post Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    store_manager_id = models.CharField(db_column='Store Manager ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    store_open_from = models.DateTimeField(db_column='Store Open from')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    store_open_to = models.DateTimeField(db_column='Store Open to')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_no_field = models.CharField(db_column='Phone No_', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    country_code = models.CharField(db_column='Country Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    global_dimension_1_code = models.CharField(db_column='Global Dimension 1 Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_code = models.CharField(db_column='Location Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code = models.CharField(db_column='Currency Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    global_dimension_2_code = models.CharField(db_column='Global Dimension 2 Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    store_open_after_midnight = models.SmallIntegerField(db_column='Store Open After Midnight')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_date_modified = models.DateTimeField(db_column='Last Date Modified')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pos_func_profile = models.CharField(db_column='POS Func_ Profile', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    li_lo_in_transaction = models.SmallIntegerField(db_column='LI_LO in Transaction')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    no_series = models.CharField(db_column='No_ Series', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    statement_nos_field = models.CharField(db_column='Statement Nos_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    one_statement_per_day = models.SmallIntegerField(db_column='One Statement per Day')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    statement_method = models.IntegerField(db_column='Statement Method')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    closing_method = models.IntegerField(db_column='Closing Method')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rounding_account = models.CharField(db_column='Rounding Account', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    max_diff_to_allow_post_field = models.DecimalField(db_column='Max_ Diff_ to Allow Post_', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    max_round_in_stmt_field = models.DecimalField(db_column='Max_ Round_ in Stmt_', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    max_diff_from_shift_date = models.DecimalField(db_column='Max_ Diff_ from Shift Date', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allowed_diff_in_trans_field = models.DecimalField(db_column='Allowed Diff_ in Trans_', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tend_decl_calculation = models.IntegerField(db_column='Tend_ Decl_ Calculation')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_discount_tender = models.CharField(db_column='Total Discount Tender', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xremove_add_tender = models.CharField(db_column='xRemove_Add Tender', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    create_labels_for_0_price = models.SmallIntegerField(db_column='Create Labels for 0 Price')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    campaign_nos_field = models.CharField(db_column='Campaign Nos_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    promotion_nos_field = models.CharField(db_column='Promotion Nos_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    periodic_discount_nos_field = models.CharField(db_column='Periodic Discount Nos_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pos_terminal_nos_field = models.CharField(db_column='POS Terminal Nos_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    staff_id_nos_field = models.CharField(db_column='Staff ID Nos_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    coupon_nos_field = models.CharField(db_column='Coupon Nos_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    item_nos_field = models.CharField(db_column='Item Nos_', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    data_access_control = models.SmallIntegerField(db_column='Data Access Control')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    store_vat_bus_post_gr_field = models.CharField(db_column='Store VAT Bus_ Post_ Gr_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    store_gen_bus_post_gr_field = models.CharField(db_column='Store Gen_ Bus_ Post_ Gr_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    language_code = models.CharField(db_column='Language Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pos_inventory_lookup = models.SmallIntegerField(db_column='POS Inventory Lookup')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rcpt_text_max_length = models.IntegerField(db_column='Rcpt_ Text Max_ Length')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    no_of_top_bottom_lines = models.IntegerField(db_column='No_ of Top_Bottom Lines')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_no_on_receipt = models.IntegerField(db_column='Item No_ on Receipt')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_action_for_label_upd = models.IntegerField(db_column='Last Action for Label Upd')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_action_for_item_label_upd = models.IntegerField(db_column='Last Action for Item Label Upd')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    no_shelf_label_printing = models.SmallIntegerField(db_column='No Shelf Label Printing')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    no_item_label_printing = models.SmallIntegerField(db_column='No Item Label Printing')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_charge_field = models.DecimalField(db_column='Service Charge %', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    serv_charge_inc_exp_acc = models.CharField(db_column='Serv_ Charge_ Inc_Exp Acc', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_charge_prompt = models.CharField(db_column='Service Charge Prompt', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customs_nos = models.CharField(db_column='Customs  Nos', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_shift = models.CharField(db_column='Current Shift', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    e_mail_address = models.CharField(db_column='E-mail Address', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pos_nos = models.CharField(db_column='POS Nos', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pos_posting_nos = models.CharField(db_column='POS Posting Nos', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pos_shipping_nos = models.CharField(db_column='POS Shipping Nos', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    automatic_drawer_creation = models.IntegerField(db_column='Automatic Drawer Creation')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    automatic_salesperson_creation = models.IntegerField(db_column='Automatic Salesperson Creation')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    store_size_square_meters_field = models.IntegerField(db_column='Store size (square meters)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    xno_of_tables_columns_field = models.IntegerField(db_column='xNo_ of Tables (Columns)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    xrestaurant_layout = models.BinaryField(db_column='xRestaurant Layout', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xno_of_tables_rows_field = models.IntegerField(db_column='xNo_ of Tables (Rows)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    show_sales_price = models.DecimalField(db_column='Show Sales Price', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    receiving_nos_field = models.CharField(db_column='Receiving Nos_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    posted_receiving_nos_field = models.CharField(db_column='Posted Receiving Nos_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    def_bom_method = models.IntegerField(db_column='Def_ BOM Method')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gift_registration_nos_field = models.CharField(db_column='Gift Registration Nos_', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    use_batch_posting_for_statem_field = models.SmallIntegerField(db_column='Use Batch Posting for Statem_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    only_accept_statement = models.SmallIntegerField(db_column='Only Accept Statement')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    max_diff_to_allow_accept = models.DecimalField(db_column='Max_ Diff_ to Allow Accept', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_hosp_printing_route = models.CharField(db_column='Current Hosp_ Printing Route', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pos_start_amount_method = models.IntegerField(db_column='POS Start Amount Method')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    post_to_bank_account = models.SmallIntegerField(db_column='Post to Bank Account')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ordering_status = models.IntegerField(db_column='Ordering Status')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Store'
        unique_together = (('location_code', 'no_field'),)


class AthlStoreGroup(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    code = models.CharField(db_column='Code', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    distribution_group_code = models.CharField(db_column='Distribution Group Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distribution_subgroup_code = models.CharField(db_column='Distribution Subgroup Code', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Store Group'
        unique_together = (('type', 'code'),)


class AthlSveitakeppniHlaups(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót_götuhlaup = models.CharField(db_column='Mót _ Götuhlaup', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    númer = models.IntegerField(db_column='Númer')  # Field name made lowercase.
    heiti_sveitar = models.CharField(db_column='Heiti sveitar', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    aldur_frá = models.IntegerField(db_column='Aldur frá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_til = models.IntegerField(db_column='Aldur til')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fjöldi_í_sveit = models.IntegerField(db_column='Fjöldi í sveit')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    félagasveitir = models.SmallIntegerField(db_column='Félagasveitir')  # Field name made lowercase.
    útreikningur = models.IntegerField(db_column='Útreikningur')  # Field name made lowercase.
    keppnisflokkur = models.IntegerField(db_column='Keppnisflokkur')  # Field name made lowercase.
    aðeins_taka_gildar_sveitir = models.SmallIntegerField(db_column='Aðeins taka gildar sveitir')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lágmarksfjöldi_karla_bæði_field = models.IntegerField(db_column='Lágmarksfjöldi karla (bæði)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lágmarksfjöldi_kvenna_bæði_field = models.IntegerField(db_column='Lágmarksfjöldi kvenna (bæði)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'Athl$Sveitakeppni hlaups'
        unique_together = (('mót_götuhlaup', 'númer'),)


class AthlT10Greinar(models.Model):
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    röð = models.CharField(db_column='Röð', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$T10Greinar'


class AthlTestkeppmti(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mot = models.CharField(primary_key=True, max_length=10)
    rasnumer = models.IntegerField()
    keppendanumer = models.CharField(max_length=10)
    nafn = models.CharField(max_length=35)
    felag = models.CharField(max_length=10)
    felaginnansambands = models.CharField(max_length=10)
    kyn = models.IntegerField()
    kennitala = models.CharField(max_length=11)
    faedingardagur = models.DateTimeField()
    faedingarar = models.IntegerField()
    aldurkeppanda = models.IntegerField()
    aldursflokkur = models.IntegerField()
    leitarnafn = models.CharField(max_length=35)
    land = models.CharField(max_length=10)
    keppnisflokkurihlaupi = models.CharField(max_length=11)
    timinumeriskur = models.DecimalField(max_digits=38, decimal_places=20)
    timi = models.CharField(max_length=12)
    rodimark = models.IntegerField()
    rodiflokki = models.IntegerField()
    heitisveitar = models.CharField(max_length=50)
    ogreittthatttokugjald = models.SmallIntegerField()
    skraning = models.IntegerField()
    vegalengd = models.CharField(max_length=10)
    keppnisflokkur = models.IntegerField()
    skogerd = models.IntegerField()
    staerdtbols = models.IntegerField()
    athugasemd = models.CharField(max_length=50)
    numerflogu = models.CharField(max_length=10)
    starttimiklst = models.CharField(max_length=15)
    lokatimiklst = models.CharField(max_length=15)
    nettotimi = models.CharField(max_length=15)
    kaupaedaleigjaflogu = models.IntegerField()
    bruttotimi = models.CharField(max_length=15)
    bodhlaupssveit = models.SmallIntegerField()
    fyrirlidi = models.SmallIntegerField()
    millitimi1klst = models.CharField(max_length=15)
    millitimi1brutto = models.CharField(max_length=15)
    millitimi1netto = models.CharField(max_length=15)
    millitimi2klst = models.CharField(max_length=15)
    millitimi2brutto = models.CharField(max_length=15)
    millitimi2netto = models.CharField(max_length=15)
    byssutimihlaupara = models.CharField(max_length=30)
    millitimi3klst = models.CharField(max_length=15)
    millitimi3brutto = models.CharField(max_length=15)
    millitimi3netto = models.CharField(max_length=15)
    rasnumeraskyrslu = models.IntegerField()
    wrkheimili = models.CharField(max_length=50)
    wrkstadur = models.CharField(max_length=50)
    vantarbol = models.SmallIntegerField()
    gestur = models.SmallIntegerField()
    skraningardags = models.DateTimeField()
    skraningartimi = models.DateTimeField()
    skradaf = models.CharField(max_length=10)
    wrkemail = models.CharField(max_length=50)
    flokkurhlaups = models.CharField(max_length=10)
    staerdbolstexti = models.CharField(db_column='StaerdBolsTexti', max_length=30)  # Field name made lowercase.
    medrutu = models.SmallIntegerField(db_column='MedRutu')  # Field name made lowercase.
    idegauserid = models.CharField(db_column='IDEGAUserID', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$TESTKeppÍMóti'
        unique_together = (('mot', 'rasnumer'), ('keppendanumer', 'mot', 'rasnumer'), ('mot', 'kyn', 'keppnisflokkurihlaupi', 'rasnumer'), ('mot', 'felag', 'rodimark', 'rasnumer'), ('mot', 'rodimark', 'rasnumer'), ('mot', 'heitisveitar', 'rodimark', 'rasnumer'), ('mot', 'numerflogu', 'rasnumer'), ('mot', 'kyn', 'nafn', 'rasnumer'), ('mot', 'lokatimiklst', 'nettotimi', 'rasnumer'), ('kennitala', 'leitarnafn', 'mot', 'rasnumer'),)


class AthlTableDistributionSetup(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    table_id = models.IntegerField(db_column='Table ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    master_table_id = models.IntegerField(db_column='Master Table ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distribution_type = models.IntegerField(db_column='Distribution Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    no_actions = models.SmallIntegerField(db_column='No Actions')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actions_on_linked_tables = models.SmallIntegerField(db_column='Actions on Linked Tables')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    linked_actions_on_insert = models.SmallIntegerField(db_column='Linked Actions on Insert')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    linked_actions_on_modify = models.SmallIntegerField(db_column='Linked Actions on Modify')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    linked_actions_on_delete = models.SmallIntegerField(db_column='Linked Actions on Delete')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indentation = models.IntegerField(db_column='Indentation')  # Field name made lowercase.
    sorting_key = models.CharField(db_column='Sorting Key', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preaction_key = models.IntegerField(db_column='Preaction Key')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Table Distribution Setup'
        unique_together = (('table_id', 'master_table_id'), ('master_table_id', 'table_id'), ('sorting_key', 'table_id', 'master_table_id'),)


class AthlTegundMts(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    tákn = models.CharField(db_column='Tákn', primary_key=True, max_length=10)  # Field name made lowercase.
    heiti = models.CharField(db_column='Heiti', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Tegund móts'


class AthlTempblob(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    primay_key = models.IntegerField(db_column='Primay Key', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    blob = models.BinaryField(db_column='Blob', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$TempBlob'


class AthlTop10PrAldursflokkRm2016(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    aldursflokkur = models.CharField(db_column='Aldursflokkur', max_length=100)  # Field name made lowercase.
    röð = models.IntegerField(db_column='Röð')  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=10)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=50)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    ísland = models.SmallIntegerField(db_column='Ísland')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Top 10 pr aldursflokk RM2016'
        unique_together = (('grein', 'kyn', 'flokkur', 'úti_inni', 'aldursflokkur', 'lína'), ('keppandanúmer', 'röð', 'lína'),)


class AthlToplist(models.Model):
    listi = models.CharField(db_column='Listi', max_length=30, blank=True, null=True)  # Field name made lowercase.
    row = models.BigIntegerField(db_column='Row', blank=True, null=True)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=10)  # Field name made lowercase.
    vindur = models.DecimalField(db_column='Vindur', max_digits=38, decimal_places=20)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    ár = models.IntegerField(db_column='Ár', blank=True, null=True)  # Field name made lowercase.
    dags = models.DateField(db_column='Dags', blank=True, null=True)  # Field name made lowercase.
    ár_síðan = models.IntegerField(db_column='Ár Síðan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    heiti_móts = models.CharField(db_column='Heiti Móts', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_keppanda = models.IntegerField(db_column='Aldur keppanda')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nafnár = models.CharField(db_column='NafnÁr', max_length=39, blank=True, null=True)  # Field name made lowercase.
    raðsvæði = models.DecimalField(db_column='Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$TopList'


class AthlTmabk(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót_götuhlaup = models.CharField(db_column='Mót _ Götuhlaup', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    rásnúmer = models.IntegerField(db_column='Rásnúmer')  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    tími = models.IntegerField(db_column='Tími')  # Field name made lowercase.
    tími_2 = models.CharField(db_column='Tími 2', max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð = models.IntegerField(db_column='Röð')  # Field name made lowercase.
    leitarnafn = models.CharField(db_column='Leitarnafn', max_length=30)  # Field name made lowercase.
    tékktími = models.SmallIntegerField(db_column='Tékktími')  # Field name made lowercase.
    leita_að_númeri = models.IntegerField(db_column='Leita að númeri')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    systurhlaup = models.CharField(db_column='Systurhlaup', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    heiti_flokks = models.CharField(db_column='Heiti Flokks', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    tákn_systurhlaups = models.CharField(db_column='Tákn systurhlaups', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    innsleginn_tími = models.IntegerField(db_column='Innsleginn tími')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    þegar_færður_á_hlaupara = models.SmallIntegerField(db_column='Þegar færður á hlaupara')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    röð_í_flokki = models.IntegerField(db_column='Röð í flokki')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    númer_flögu = models.CharField(db_column='Númer flögu', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tími_útfylltur = models.SmallIntegerField(db_column='Tími útfylltur')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    frá_klukkuskrá = models.SmallIntegerField(db_column='Frá klukkuskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sama_klukkuskráalína = models.SmallIntegerField(db_column='Sama klukkuskráalína')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    matcha_við_fyrstu_klukkuskr_lí = models.SmallIntegerField(db_column='Matcha við fyrstu klukkuskr_lí')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Tímabók'
        unique_together = (('mót_götuhlaup', 'lína'), ('mót_götuhlaup', 'rásnúmer', 'lína'), ('mót_götuhlaup', 'kyn', 'heiti_flokks', 'röð_í_flokki', 'lína'), ('mót_götuhlaup', 'tími_útfylltur', 'lína'), ('mót_götuhlaup', 'tími', 'lína'), ('mót_götuhlaup', 'innsleginn_tími', 'lína'),)


class AthlTmaseillMtsWwwMotFri(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    heit_móts = models.CharField(db_column='Heit móts', primary_key=True, max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    heiti_greinar = models.CharField(db_column='Heiti greinar', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    aldur_frá = models.IntegerField(db_column='Aldur frá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_til = models.IntegerField(db_column='Aldur til')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tími = models.DateTimeField(db_column='Tími')  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    riðill = models.IntegerField(db_column='Riðill')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Tímaseðill móts í www_mot_fri'
        unique_together = (('heit_móts', 'dagsetning', 'lína'), ('heit_móts', 'dagsetning', 'grein', 'kyn', 'flokkur', 'úti_inni', 'aldur_frá', 'aldur_til', 'riðill', 'lína'),)


class AthlUppsetningAfrekaskra(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    úti_inni = models.IntegerField(db_column='Úti_Inni', primary_key=True)  # Field name made lowercase.
    tákn = models.CharField(db_column='Tákn', max_length=10)  # Field name made lowercase.
    drög_eða_endanleg = models.IntegerField(db_column='Drög eða endanleg')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_afrekaskrár = models.CharField(db_column='Heiti afrekaskrár', max_length=70)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_afrekaskrár_ensk = models.CharField(db_column='Heiti afrekaskrár - ensk', max_length=70)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_skráa = models.CharField(db_column='Slóð skráa', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_skráa_ensk = models.CharField(db_column='Slóð skráa - ensk', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dagsetningaafmörkun = models.CharField(db_column='Dagsetningaafmörkun', max_length=30)  # Field name made lowercase.
    hámarksfjöldi_pr_grein = models.IntegerField(db_column='Hámarksfjöldi pr_ grein')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hámarksfjöldi_vindárangra = models.IntegerField(db_column='Hámarksfjöldi vindárangra')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hámarksfjöldi_handtíma = models.IntegerField(db_column='Hámarksfjöldi handtíma')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fj_samein_hand_og_rafm_field = models.IntegerField(db_column='Fj_ samein_ hand og rafm_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hámarksfjöldi_erl_ríkisborgar = models.IntegerField(db_column='Hámarksfjöldi erl_ ríkisborgar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dagsetningaafmörkun_móta = models.CharField(db_column='Dagsetningaafmörkun móta', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_afrekaskrár_öldunga = models.CharField(db_column='Heiti afrekaskrár öldunga', max_length=70)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_afrekaskrár_öldung_ensk = models.CharField(db_column='Heiti afrekaskrár öldung- ensk', max_length=70)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Uppsetning afrekaskráa'
        unique_together = (('úti_inni', 'tákn'),)


class AthlUppsetningAfrekaskra2011(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    úti_inni = models.IntegerField(db_column='Úti_Inni', primary_key=True)  # Field name made lowercase.
    tákn = models.CharField(db_column='Tákn', max_length=10)  # Field name made lowercase.
    drög_eða_endanleg = models.IntegerField(db_column='Drög eða endanleg')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_afrekaskrár = models.CharField(db_column='Heiti afrekaskrár', max_length=70)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_afrekaskrár_ensk = models.CharField(db_column='Heiti afrekaskrár - ensk', max_length=70)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_skráa = models.CharField(db_column='Slóð skráa', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    slóð_skráa_ensk = models.CharField(db_column='Slóð skráa - ensk', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dagsetningaafmörkun = models.CharField(db_column='Dagsetningaafmörkun', max_length=30)  # Field name made lowercase.
    hámarksfjöldi_pr_grein = models.IntegerField(db_column='Hámarksfjöldi pr_ grein')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hámarksfjöldi_vindárangra = models.IntegerField(db_column='Hámarksfjöldi vindárangra')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hámarksfjöldi_handtíma = models.IntegerField(db_column='Hámarksfjöldi handtíma')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fj_samein_hand_og_rafm_field = models.IntegerField(db_column='Fj_ samein_ hand og rafm_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hámarksfjöldi_erl_ríkisborgar = models.IntegerField(db_column='Hámarksfjöldi erl_ ríkisborgar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dagsetningaafmörkun_móta = models.CharField(db_column='Dagsetningaafmörkun móta', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_afrekaskrár_öldunga = models.CharField(db_column='Heiti afrekaskrár öldunga', max_length=70)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_afrekaskrár_öldung_ensk = models.CharField(db_column='Heiti afrekaskrár öldung- ensk', max_length=70)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Uppsetning afrekaskráa 2011'
        unique_together = (('úti_inni', 'tákn'),)


class AthlUserSetup(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    user_id = models.CharField(db_column='User ID', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allow_posting_from = models.DateTimeField(db_column='Allow Posting From')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allow_posting_to = models.DateTimeField(db_column='Allow Posting To')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    register_time = models.SmallIntegerField(db_column='Register Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    main_menu_id = models.IntegerField(db_column='Main Menu ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allow_fa_posting_from = models.DateTimeField(db_column='Allow FA Posting From')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allow_fa_posting_to = models.DateTimeField(db_column='Allow FA Posting To')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$User Setup'


class AthlUserTimeRegister(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    user_id = models.CharField(db_column='User ID', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    minutes = models.DecimalField(db_column='Minutes', max_digits=38, decimal_places=20)  # Field name made lowercase.
    login_date = models.DateTimeField(db_column='Login Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    login_time = models.DateTimeField(db_column='Login Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    logout_date = models.DateTimeField(db_column='Logout Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    logout_time = models.DateTimeField(db_column='Logout Time')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$User Time Register'
        unique_together = (('user_id', 'date'),)


class AthlUseraccess(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    accesslevel = models.IntegerField(db_column='AccessLevel')  # Field name made lowercase.
    e_mail = models.CharField(db_column='E-Mail', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    established = models.DateTimeField(db_column='Established')  # Field name made lowercase.
    selectedcompetition = models.CharField(db_column='SelectedCompetition', max_length=10)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$UserAccess'


class AthlUseraccessclubs(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    username = models.CharField(db_column='UserName', primary_key=True, max_length=50)  # Field name made lowercase.
    club = models.CharField(db_column='Club', max_length=10)  # Field name made lowercase.
    héraðssamband = models.CharField(db_column='Héraðssamband', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$UserAccessClubs'
        unique_together = (('username', 'club'),)


class AthlUseraccesslog(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lineno = models.IntegerField(db_column='LineNo', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    dateandtime = models.DateTimeField(db_column='DateAndTime')  # Field name made lowercase.
    correctpassword = models.SmallIntegerField(db_column='CorrectPassword')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$UserAccessLog'


class AthlVallarmet(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    land = models.CharField(db_column='Land', primary_key=True, max_length=10)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    dagsetning_mets = models.DateTimeField(db_column='Dagsetning mets')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=20)  # Field name made lowercase.
    árangur_raðsvæði = models.DecimalField(db_column='Árangur raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    staður_mets = models.CharField(db_column='Staður mets', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    methafi = models.CharField(db_column='Methafi', max_length=10)  # Field name made lowercase.
    heiti_methafa = models.CharField(db_column='Heiti methafa', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    félag_methafa = models.CharField(db_column='Félag methafa', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sería_eða_skipan_boðhlaupssv_field = models.CharField(db_column='Sería eða skipan boðhlaupssv_', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    röð_í_afrekaskrá = models.DecimalField(db_column='Röð í afrekaskrá', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kennitala_methafa = models.CharField(db_column='Kennitala methafa', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fæðingarár_methafa = models.IntegerField(db_column='Fæðingarár methafa')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_methafa = models.IntegerField(db_column='Aldur methafa')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    óstaðfest = models.SmallIntegerField(db_column='Óstaðfest')  # Field name made lowercase.
    innelsinn_árangur = models.CharField(db_column='Innelsinn árangur', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    landssveit = models.SmallIntegerField(db_column='Landssveit')  # Field name made lowercase.
    línunr_í_afrekum = models.IntegerField(db_column='Línunr_ í afrekum')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vindur = models.DecimalField(db_column='Vindur', max_digits=38, decimal_places=20)  # Field name made lowercase.
    virkt = models.SmallIntegerField(db_column='Virkt')  # Field name made lowercase.
    met_í_flokki = models.IntegerField(db_column='Met í flokki')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    línunúmer = models.IntegerField(db_column='Línunúmer')  # Field name made lowercase.
    athugasemd = models.CharField(db_column='Athugasemd', max_length=30)  # Field name made lowercase.
    athugasemd_ensk = models.CharField(db_column='Athugasemd Ensk', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keppnisvöllur = models.CharField(db_column='Keppnisvöllur', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Vallarmet'
        unique_together = (('land', 'grein', 'kyn', 'flokkur', 'úti_inni', 'dagsetning_mets', 'lína'), ('grein', 'kyn', 'flokkur', 'land', 'dagsetning_mets', 'úti_inni', 'lína'), ('land', 'kyn', 'flokkur', 'röð_í_afrekaskrá', 'grein', 'úti_inni', 'dagsetning_mets', 'lína'), ('methafi', 'grein', 'flokkur', 'úti_inni', 'dagsetning_mets', 'land', 'kyn', 'lína'), ('úti_inni', 'met_í_flokki', 'röð_í_afrekaskrá', 'land', 'grein', 'kyn', 'flokkur', 'dagsetning_mets', 'lína'), ('methafi', 'dagsetning_mets', 'land', 'grein', 'kyn', 'flokkur', 'úti_inni', 'lína'),)


class AthlVantarAFlytja(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót = models.CharField(db_column='Mót', primary_key=True, max_length=20)  # Field name made lowercase.
    heiti = models.CharField(db_column='Heiti', max_length=50)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    hlaup_mót = models.IntegerField(db_column='Hlaup_Mót')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Vantar að flytja'


class AthlVenjulegarKeppnisgrldunga(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    aldursflokkur_öldunga = models.CharField(db_column='Aldursflokkur öldunga', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    röð_í_afrekaskra = models.IntegerField(db_column='Röð í afrekaskra')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Venjulegar keppnisgr öldunga'
        unique_together = (('aldursflokkur_öldunga', 'grein', 'kyn', 'flokkur', 'úti_inni'), ('aldursflokkur_öldunga', 'röð_í_afrekaskra', 'grein', 'kyn', 'flokkur', 'úti_inni'),)


class AthlVenues(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    heiti = models.CharField(db_column='Heiti', primary_key=True, max_length=50)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    hringhlaup_á_hallandi_braut = models.SmallIntegerField(db_column='Hringhlaup á hallandi braut')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fj_hringbrauta_spretthlaup = models.IntegerField(db_column='Fj_ hringbrauta spretthlaup')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fjöldi_beinna_brauta = models.IntegerField(db_column='Fjöldi beinna brauta')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    opnunardagsetning = models.DateTimeField(db_column='Opnunardagsetning')  # Field name made lowercase.
    fj_hingbrauta_millivegalengd = models.IntegerField(db_column='Fj_ hingbrauta millivegalengd')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fj_hringbrauta_langhlaup = models.IntegerField(db_column='Fj_ hringbrauta langhlaup')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Venues'


class AthlVinnuskrFyrirWwwFriIs(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    tegund = models.IntegerField(db_column='Tegund', primary_key=True)  # Field name made lowercase.
    field_1 = models.CharField(db_column='Field 1', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_2 = models.CharField(db_column='Field 2', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_3 = models.CharField(db_column='Field 3', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_4 = models.CharField(db_column='Field 4', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_5 = models.CharField(db_column='Field 5', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_6 = models.CharField(db_column='Field 6', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_7 = models.CharField(db_column='Field 7', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_8 = models.CharField(db_column='Field 8', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_9 = models.CharField(db_column='Field 9', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_10 = models.CharField(db_column='Field 10', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_11 = models.CharField(db_column='Field 11', max_length=35)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_12 = models.CharField(db_column='Field 12', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_13 = models.CharField(db_column='Field 13', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_14 = models.CharField(db_column='Field 14', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_15 = models.CharField(db_column='Field 15', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_16 = models.CharField(db_column='Field 16', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_17 = models.CharField(db_column='Field 17', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_18 = models.CharField(db_column='Field 18', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_19 = models.CharField(db_column='Field 19', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_20 = models.CharField(db_column='Field 20', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_21 = models.CharField(db_column='Field 21', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_22 = models.CharField(db_column='Field 22', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_23 = models.CharField(db_column='Field 23', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_24 = models.CharField(db_column='Field 24', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_25 = models.CharField(db_column='Field 25', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Vinnuskrá fyrir WWW_FRI_IS'
        unique_together = (('tegund', 'field_1', 'field_2', 'field_3'),)


class AthlVinnuskrFyrirAfrekaskr(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=20)  # Field name made lowercase.
    vindur = models.DecimalField(db_column='Vindur', max_digits=38, decimal_places=20)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=50)  # Field name made lowercase.
    fæðingardagur = models.DateTimeField(db_column='Fæðingardagur')  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    mót = models.CharField(db_column='Mót', max_length=10)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=50)  # Field name made lowercase.
    heiti_móts = models.CharField(db_column='Heiti móts', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldursflokkur = models.CharField(db_column='Aldursflokkur', max_length=30)  # Field name made lowercase.
    löglegt = models.SmallIntegerField(db_column='Löglegt')  # Field name made lowercase.
    stig = models.IntegerField(db_column='Stig')  # Field name made lowercase.
    röð_í_flokki = models.IntegerField(db_column='Röð í flokki')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldurstexti = models.CharField(db_column='Aldurstexti', max_length=50)  # Field name made lowercase.
    wma_field = models.DecimalField(db_column='WMA %', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    erlendur_ríkisborgari = models.SmallIntegerField(db_column='Erlendur ríkisborgari')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Vinnuskrá fyrir afrekaskrá'
        unique_together = (('kyn', 'wma_field', 'lína'),)


class AthlVinnuskrFyrirRun(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lykill = models.CharField(db_column='Lykill', primary_key=True, max_length=50)  # Field name made lowercase.
    lína = models.DecimalField(db_column='Lína', max_digits=38, decimal_places=20)  # Field name made lowercase.
    tala_1 = models.DecimalField(db_column='Tala 1', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tala_2 = models.DecimalField(db_column='Tala 2', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tala_3 = models.DecimalField(db_column='Tala 3', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tala_4 = models.DecimalField(db_column='Tala 4', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tala_5 = models.DecimalField(db_column='Tala 5', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tala_6 = models.DecimalField(db_column='Tala 6', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer = models.IntegerField(db_column='Rásnúmer')  # Field name made lowercase.
    lína_2 = models.DecimalField(db_column='Lína 2', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    riðill = models.IntegerField(db_column='Riðill')  # Field name made lowercase.
    braut = models.IntegerField(db_column='Braut')  # Field name made lowercase.
    texti = models.CharField(db_column='Texti', max_length=80)  # Field name made lowercase.
    texti_2 = models.CharField(db_column='Texti 2', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    metrar = models.DecimalField(db_column='Metrar', max_digits=38, decimal_places=20)  # Field name made lowercase.
    texti_3 = models.CharField(db_column='Texti 3', max_length=250)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jánei_1 = models.SmallIntegerField(db_column='JáNei 1')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    athugasemd = models.CharField(db_column='Athugasemd', max_length=100)  # Field name made lowercase.
    qualification = models.CharField(db_column='Qualification', max_length=30)  # Field name made lowercase.
    teljari = models.IntegerField(db_column='Teljari')  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    teljari2 = models.IntegerField(db_column='Teljari2')  # Field name made lowercase.
    teljari3 = models.IntegerField(db_column='Teljari3')  # Field name made lowercase.
    teljari4 = models.IntegerField(db_column='Teljari4')  # Field name made lowercase.
    línunúmer = models.IntegerField(db_column='Línunúmer')  # Field name made lowercase.
    decimal1 = models.DecimalField(db_column='Decimal1', max_digits=38, decimal_places=20)  # Field name made lowercase.
    decimal2 = models.DecimalField(db_column='Decimal2', max_digits=38, decimal_places=20)  # Field name made lowercase.
    tákn = models.CharField(db_column='Tákn', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Vinnuskrá fyrir röðun'
        unique_together = (('lykill', 'lína', 'tala_1', 'tala_2', 'tala_3', 'tala_4', 'tala_5', 'tala_6', 'rásnúmer', 'lína_2'), ('riðill', 'braut', 'lykill', 'lína', 'tala_1', 'tala_2', 'tala_3', 'tala_4', 'tala_5', 'tala_6', 'rásnúmer', 'lína_2'), ('dagsetning', 'lykill', 'lína', 'tala_1', 'tala_2', 'tala_3', 'tala_4', 'tala_5', 'tala_6', 'rásnúmer', 'lína_2'), ('tala_1', 'tala_2', 'tala_3', 'lykill', 'lína', 'tala_4', 'tala_5', 'tala_6', 'rásnúmer', 'lína_2'), ('línunúmer', 'teljari', 'lykill', 'lína', 'tala_1', 'tala_2', 'tala_3', 'tala_4', 'tala_5', 'tala_6', 'rásnúmer', 'lína_2'), ('tala_2', 'lykill', 'lína', 'tala_1', 'tala_3', 'tala_4', 'tala_5', 'tala_6', 'rásnúmer', 'lína_2'), ('decimal2', 'lykill', 'lína', 'tala_1', 'tala_2', 'tala_3', 'tala_4', 'tala_5', 'tala_6', 'rásnúmer', 'lína_2'), ('tákn', 'dagsetning', 'lykill', 'lína', 'tala_1', 'tala_2', 'tala_3', 'tala_4', 'tala_5', 'tala_6', 'rásnúmer', 'lína_2'),)


class AthlWrkTmaseillMeMeti(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    raðsv2 = models.AutoField(db_column='Raðsv2', primary_key=True)  # Field name made lowercase.
    tími = models.CharField(db_column='Tími', max_length=30)  # Field name made lowercase.
    heiti_greinar = models.CharField(db_column='Heiti Greinar', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldursflokkur = models.CharField(db_column='Aldursflokkur', max_length=30)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    aldur_frá = models.IntegerField(db_column='Aldur frá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aldur_til = models.IntegerField(db_column='Aldur til')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    raðsv = models.IntegerField(db_column='Raðsv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Wrk Tímaseðill með meti'
        unique_together = (('lína', 'raðsv2'), ('raðsv', 'lína', 'raðsv2'), ('tími', 'heiti_greinar', 'lína', 'raðsv2'),)


class AthlXmlDataBuffer(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    entry_no_field = models.IntegerField(db_column='Entry No_', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    nodename = models.CharField(db_column='NodeName', max_length=50)  # Field name made lowercase.
    row_no_field = models.IntegerField(db_column='Row No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=250)  # Field name made lowercase.
    attribute_name = models.CharField(db_column='Attribute Name', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'Athl$XML Data Buffer'
        unique_together = (('nodename', 'row_no_field', 'level', 'entry_no_field'),)


class AthlFlogurhlaups(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    flokkurhlaups = models.CharField(primary_key=True, max_length=10)
    rasnumer = models.IntegerField()
    flogunumer = models.CharField(max_length=10)
    dagsetninghlaups = models.DateTimeField()
    skraningardagsetning = models.DateTimeField()
    skraningartimi = models.DateTimeField()
    heitiskrar = models.CharField(max_length=30)
    eiginflaga = models.CharField(max_length=10)
    aths = models.CharField(db_column='Aths', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$flogurhlaups'
        unique_together = (('flokkurhlaups', 'rasnumer'), ('flogunumer', 'dagsetninghlaups', 'flokkurhlaups', 'rasnumer'), ('flokkurhlaups', 'flogunumer', 'rasnumer'),)


class AthlFloguskra(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    flogunumer = models.CharField(primary_key=True, max_length=10)
    numerkeppanda = models.CharField(max_length=10)
    liturflogu = models.IntegerField()
    skraningardagsetning = models.DateTimeField()
    skraningartimi = models.DateTimeField()
    soluadili = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Athl$floguskra'
        unique_together = (('numerkeppanda', 'flogunumer'),)


class AthlFlokkarhlaups(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    flokkur = models.CharField(db_column='Flokkur', primary_key=True, max_length=10)  # Field name made lowercase.
    heiti = models.CharField(db_column='Heiti', max_length=30)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning')  # Field name made lowercase.
    rásnúmer_frá_1 = models.IntegerField(db_column='Rásnúmer Frá 1')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_til_1 = models.IntegerField(db_column='Rásnúmer Til 1')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_hlaups_1 = models.CharField(db_column='Tákn Hlaups 1', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_frá_2 = models.IntegerField(db_column='Rásnúmer Frá 2')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_til_2 = models.IntegerField(db_column='Rásnúmer Til 2')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_hlaups_2 = models.CharField(db_column='Tákn Hlaups 2', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_frá_3 = models.IntegerField(db_column='Rásnúmer Frá 3')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_til_3 = models.IntegerField(db_column='Rásnúmer Til 3')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_hlaups_3 = models.CharField(db_column='Tákn Hlaups 3', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_frá_4 = models.IntegerField(db_column='Rásnúmer Frá 4')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_til_4 = models.IntegerField(db_column='Rásnúmer Til 4')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_hlaups_4 = models.CharField(db_column='Tákn Hlaups 4', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_frá_5 = models.IntegerField(db_column='Rásnúmer Frá 5')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_til_5 = models.IntegerField(db_column='Rásnúmer Til 5')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_hlaups_5 = models.CharField(db_column='Tákn Hlaups 5', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_frá_6 = models.IntegerField(db_column='Rásnúmer Frá 6')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_til_6 = models.IntegerField(db_column='Rásnúmer Til 6')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_hlaups_6 = models.CharField(db_column='Tákn Hlaups 6', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_frá_7 = models.IntegerField(db_column='Rásnúmer Frá 7')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_til_7 = models.IntegerField(db_column='Rásnúmer Til 7')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_hlaups_7 = models.CharField(db_column='Tákn Hlaups 7', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_frá_8 = models.IntegerField(db_column='Rásnúmer Frá 8')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer_til_8 = models.IntegerField(db_column='Rásnúmer Til 8')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tákn_hlaups_8 = models.CharField(db_column='Tákn Hlaups 8', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    filter_fyrir_rásnúmer_hl_1 = models.CharField(db_column='Filter fyrir rásnúmer Hl 1', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    filter_fyrir_rásnúmer_hl_2 = models.CharField(db_column='Filter fyrir rásnúmer Hl 2', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    filter_fyrir_rásnúmer_hl_3 = models.CharField(db_column='Filter fyrir rásnúmer Hl 3', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    filter_fyrir_rásnúmer_hl_4 = models.CharField(db_column='Filter fyrir rásnúmer Hl 4', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    filter_fyrir_rásnúmer_hl_5 = models.CharField(db_column='Filter fyrir rásnúmer Hl 5', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    filter_fyrir_rásnúmer_hl_6 = models.CharField(db_column='Filter fyrir rásnúmer Hl 6', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    filter_fyrir_rásnúmer_hl_7 = models.CharField(db_column='Filter fyrir rásnúmer Hl 7', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    filter_fyrir_rásnúmer_hl_8 = models.CharField(db_column='Filter fyrir rásnúmer Hl 8', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    birta_með_medalíu = models.SmallIntegerField(db_column='BIrta Með medalíu')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    birta_heiti_sveitar = models.SmallIntegerField(db_column='Birta heiti sveitar')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$flokkarhlaups'


class AthlVenjulegriAfrekaskr(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    grein = models.CharField(db_column='Grein', primary_key=True, max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    aldursflokkur_frí = models.CharField(db_column='Aldursflokkur FRÍ', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    samsettur_lykill_greinar = models.CharField(db_column='Samsettur lykill greinar', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Í venjulegri afrekaskrá'
        unique_together = (('grein', 'kyn', 'flokkur', 'úti_inni', 'aldursflokkur_frí'),)


class AthlbrKeppendurRmSastar(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    kennitala = models.CharField(db_column='Kennitala', primary_key=True, max_length=20)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    lesið_nafn = models.CharField(db_column='Lesið nafn', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    fæðingardagur = models.DateTimeField(db_column='Fæðingardagur')  # Field name made lowercase.
    þjóðerni = models.CharField(db_column='Þjóðerni', max_length=30)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E-mail', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vegalengd = models.CharField(db_column='Vegalengd', max_length=30)  # Field name made lowercase.
    má_senda_e_mail = models.SmallIntegerField(db_column='Má senda e-mail')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$ÍBR keppendur RM Síðasta ár'
        unique_together = (('lína', 'kennitala'), ('keppandanúmer', 'kennitala'),)


class AthlbrKeppendurRmBohlaupi(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    kóti_hlaups = models.CharField(db_column='Kóti hlaups', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tími_sveitar = models.CharField(db_column='Tími sveitar', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heiti_sveitar = models.CharField(db_column='Heiti sveitar', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rásnúmer = models.IntegerField(db_column='Rásnúmer')  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10)  # Field name made lowercase.
    ár = models.IntegerField(db_column='Ár')  # Field name made lowercase.
    sprettur_númer = models.IntegerField(db_column='Sprettur númer')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    boðhlaupstexti = models.CharField(db_column='Boðhlaupstexti', max_length=100)  # Field name made lowercase.
    röð_í_mark = models.IntegerField(db_column='Röð í mark')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$ÍBR keppendur í RM boðhlaupi'
        unique_together = (('kóti_hlaups', 'rásnúmer', 'keppandanúmer', 'ár', 'sprettur_númer'),)


class AthlldungarNafnalisti(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    lína = models.IntegerField(db_column='Lína', primary_key=True)  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    heimili = models.CharField(db_column='Heimili', max_length=35)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    tölvupóstur = models.CharField(db_column='Tölvupóstur', max_length=50)  # Field name made lowercase.
    aths = models.CharField(db_column='Aths', max_length=30)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    sími = models.CharField(db_column='Sími', max_length=30)  # Field name made lowercase.
    sími_2 = models.CharField(db_column='Sími 2', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sími_3 = models.CharField(db_column='Sími 3', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    í_þjóðskrá = models.SmallIntegerField(db_column='Í þjóðskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keppendanúmer = models.CharField(db_column='Keppendanúmer', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Öldungar - nafnalisti'
        unique_together = (('nafn', 'lína'), ('kennitala', 'lína'),)


class AthlrslitSveitakeppni(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót_götuhlaup = models.CharField(db_column='Mót _ Götuhlaup', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    númer = models.IntegerField(db_column='Númer')  # Field name made lowercase.
    tími_sveitar = models.DecimalField(db_column='Tími sveitar', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stig_sveitar = models.DecimalField(db_column='Stig sveitar', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tími = models.CharField(db_column='Tími', max_length=15)  # Field name made lowercase.
    heiti_sveitar = models.CharField(db_column='Heiti sveitar', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    rásnúmer = models.IntegerField(db_column='Rásnúmer')  # Field name made lowercase.
    röð = models.IntegerField(db_column='Röð')  # Field name made lowercase.
    röð_1_manns = models.IntegerField(db_column='Röð 1_ manns')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keppnisflokkur = models.IntegerField(db_column='Keppnisflokkur')  # Field name made lowercase.
    röð_sveitar = models.IntegerField(db_column='Röð sveitar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stig = models.DecimalField(db_column='Stig', max_digits=38, decimal_places=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Athl$Úrslit sveitakeppni'
        unique_together = (('mót_götuhlaup', 'númer', 'tími_sveitar', 'stig_sveitar', 'tími', 'heiti_sveitar', 'nafn'), ('mót_götuhlaup', 'heiti_sveitar', 'númer', 'tími_sveitar', 'stig_sveitar', 'tími', 'nafn'), ('mót_götuhlaup', 'númer', 'tími_sveitar', 'stig_sveitar', 'röð_1_manns', 'heiti_sveitar', 'nafn', 'tími'), ('mót_götuhlaup', 'númer', 'tími_sveitar', 'stig_sveitar', 'heiti_sveitar', 'röð', 'tími', 'nafn'),)


class AthlrvalshpurUnglinga2017Plus(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    gildir_frá = models.DateTimeField(db_column='Gildir frá', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    number_15_og_16_ára = models.CharField(db_column='15 og 16 ára', max_length=30)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_ára = models.CharField(db_column='17 ára', max_length=30)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_18_ára = models.CharField(db_column='18 ára', max_length=30)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_19_ára = models.CharField(db_column='19 ára', max_length=30)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    röð_í_afrekaskrá = models.IntegerField(db_column='Röð í afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    línunúmer = models.IntegerField(db_column='Línunúmer')  # Field name made lowercase.
    number_15_og_16_ára_raðsvæði = models.DecimalField(db_column='15 og 16 ára raðsvæði', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_ára_raðsvæði = models.DecimalField(db_column='17 ára raðsvæði', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_18_ára_raðsvæði = models.DecimalField(db_column='18 ára raðsvæði', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_19_ára_raðsvæði = models.DecimalField(db_column='19 ára raðsvæði', max_digits=38, decimal_places=20)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'Athl$Úrvalshópur unglinga 2017 plus'
        unique_together = (('gildir_frá', 'grein', 'kyn', 'flokkur', 'úti_inni'), ('gildir_frá', 'kyn', 'röð_í_afrekaskrá', 'grein', 'flokkur', 'úti_inni'), ('línunúmer', 'gildir_frá', 'grein', 'kyn', 'flokkur', 'úti_inni'),)


class AthlrvalshpurUnglingaLgmrk(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    gildir_frá = models.DateTimeField(db_column='Gildir frá', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grein = models.CharField(db_column='Grein', max_length=10)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10)  # Field name made lowercase.
    úti_inni = models.IntegerField(db_column='Úti_Inni')  # Field name made lowercase.
    number_15_ára = models.CharField(db_column='15 ára', max_length=30)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_16_ára = models.CharField(db_column='16 ára', max_length=30)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_ára = models.CharField(db_column='17 ára', max_length=30)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_18_ára = models.CharField(db_column='18 ára', max_length=30)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_19_ára = models.CharField(db_column='19 ára', max_length=30)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_20_ára = models.CharField(db_column='20 ára', max_length=30)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_21_árs = models.CharField(db_column='21 árs', max_length=30)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_22_ára = models.CharField(db_column='22 ára', max_length=30)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    röð_í_afrekaskrá = models.IntegerField(db_column='Röð í afrekaskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    línunúmer = models.IntegerField(db_column='Línunúmer')  # Field name made lowercase.
    number_15_ára_raðsvæði = models.DecimalField(db_column='15 ára Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_16_ára_raðsvæði = models.DecimalField(db_column='16 ára Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_ára_raðsvæði = models.DecimalField(db_column='17 ára Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_18_ára_raðsvæði = models.DecimalField(db_column='18 ára Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_19_ára_raðsvæði = models.DecimalField(db_column='19 ára Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_20_ára_raðsvæði = models.DecimalField(db_column='20 ára Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_21_árs_raðsvæði = models.DecimalField(db_column='21 árs Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_22_ára_raðsvæði = models.DecimalField(db_column='22 ára Raðsvæði', max_digits=38, decimal_places=20)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'Athl$Úrvalshópur unglinga lágmörk'
        unique_together = (('gildir_frá', 'grein', 'kyn', 'flokkur', 'úti_inni'), ('gildir_frá', 'kyn', 'röð_í_afrekaskrá', 'grein', 'flokkur', 'úti_inni'), ('línunúmer', 'gildir_frá', 'grein', 'kyn', 'flokkur', 'úti_inni'),)


class Athljskrrbreytingar(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    kennitala = models.CharField(db_column='Kennitala', max_length=11)  # Field name made lowercase.
    var_verður = models.IntegerField(db_column='Var - verður')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nafn = models.CharField(db_column='Nafn', max_length=35)  # Field name made lowercase.
    heimili = models.CharField(db_column='Heimili', max_length=30)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    fjölskyldunúmer = models.CharField(db_column='Fjölskyldunúmer', max_length=11)  # Field name made lowercase.
    bannmerking = models.SmallIntegerField(db_column='Bannmerking')  # Field name made lowercase.
    íslendingur = models.SmallIntegerField(db_column='Íslendingur')  # Field name made lowercase.
    afdrif = models.CharField(db_column='Afdrif', max_length=4)  # Field name made lowercase.
    meðhöndlað = models.SmallIntegerField(db_column='Meðhöndlað')  # Field name made lowercase.
    dagsetning_breytingar = models.CharField(db_column='Dagsetning breytingar', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Athl$Þjóðskrárbreytingar'
        unique_together = (('dagsetning_breytingar', 'kennitala', 'var_verður'),)


class Chart(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    company = models.CharField(db_column='Company', primary_key=True, max_length=30)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    blob = models.BinaryField(db_column='BLOB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Chart'
        unique_together = (('company', 'id'), ('id', 'company'),)


class ClientAddIn(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    control_add_in_name = models.CharField(db_column='Control Add-in Name', primary_key=True, max_length=220)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    public_key_token = models.CharField(db_column='Public Key Token', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.CharField(db_column='Version', max_length=25)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Client Add-in'
        unique_together = (('control_add_in_name', 'public_key_token'),)


class Company(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    name = models.CharField(db_column='Name', primary_key=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Company'


class DatabaseKeyGroups(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    key_group = models.CharField(db_column='Key Group', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_change = models.IntegerField(db_column='Last Change')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Database Key Groups'


class MemberOf(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    user_id = models.CharField(db_column='User ID', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    group_id = models.CharField(db_column='Group ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    company = models.CharField(db_column='Company', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Member Of'
        unique_together = (('user_id', 'group_id', 'company'),)


class Object(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    type = models.IntegerField(db_column='Type', primary_key=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    modified = models.SmallIntegerField(db_column='Modified')  # Field name made lowercase.
    compiled = models.SmallIntegerField(db_column='Compiled')  # Field name made lowercase.
    blob_reference = models.BinaryField(db_column='BLOB Reference', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    blob_size = models.IntegerField(db_column='BLOB Size')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dbm_table_no_field = models.IntegerField(db_column='DBM Table No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    version_list = models.CharField(db_column='Version List', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    locked = models.SmallIntegerField(db_column='Locked')  # Field name made lowercase.
    locked_by = models.CharField(db_column='Locked By', max_length=132)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Object'
        unique_together = (('type', 'company_name', 'id'), ('type', 'name', 'company_name', 'id'), ('locked', 'locked_by', 'type', 'company_name', 'id'),)


class ObjectMetadata(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    object_type = models.IntegerField(db_column='Object Type', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_id = models.IntegerField(db_column='Object ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metadata = models.BinaryField(db_column='Metadata', blank=True, null=True)  # Field name made lowercase.
    version_list = models.CharField(db_column='Version List', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_code = models.BinaryField(db_column='User Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_key = models.CharField(db_column='Object Key', max_length=36)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Object Metadata'
        unique_together = (('object_type', 'object_id'),)


class ObjectTracking(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    object_type = models.IntegerField(db_column='Object Type', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_id = models.IntegerField(db_column='Object ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_key = models.CharField(db_column='Object Key', max_length=36)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_timestamp = models.BigIntegerField(db_column='Object Timestamp')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Object Tracking'
        unique_together = (('object_type', 'object_id'), ('object_timestamp', 'object_type', 'object_id'),)


class PageDataPersonalization(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    user_sid = models.CharField(db_column='User SID', primary_key=True, max_length=119)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_type = models.IntegerField(db_column='Object Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_id = models.IntegerField(db_column='Object ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    personalization_id = models.CharField(db_column='Personalization ID', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    valuename = models.CharField(db_column='ValueName', max_length=40)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    value = models.BinaryField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Page Data Personalization'
        unique_together = (('user_sid', 'object_type', 'object_id', 'personalization_id', 'valuename'), ('date', 'user_sid', 'object_type', 'object_id', 'personalization_id', 'valuename'),)


class Permission(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    group_id = models.CharField(db_column='Group ID', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_type = models.IntegerField(db_column='Object Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_id = models.IntegerField(db_column='Object ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    read_permission = models.IntegerField(db_column='Read Permission')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    insert_permission = models.IntegerField(db_column='Insert Permission')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modify_permission = models.IntegerField(db_column='Modify Permission')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delete_permission = models.IntegerField(db_column='Delete Permission')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    execute_permission = models.IntegerField(db_column='Execute Permission')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Permission'
        unique_together = (('group_id', 'object_type', 'object_id'),)


class PrinterSelection(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    user_id = models.CharField(db_column='User ID', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    report_id = models.IntegerField(db_column='Report ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    printer_name = models.CharField(db_column='Printer Name', max_length=80)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Printer Selection'
        unique_together = (('user_id', 'report_id'),)


class Product(models.Model):
    pk_id = models.IntegerField(blank=True, null=True)
    productid = models.CharField(db_column='ProductId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    productprice = models.DecimalField(db_column='ProductPrice', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class Profile(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    profile_id = models.CharField(db_column='Profile ID', primary_key=True, max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    owner_sid = models.CharField(db_column='Owner SID', max_length=119)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(db_column='Description', max_length=250)  # Field name made lowercase.
    role_center_id = models.IntegerField(db_column='Role Center ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    default_role_center = models.SmallIntegerField(db_column='Default Role Center')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Profile'


class ProfileMetadata(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    profile_id = models.CharField(db_column='Profile ID', primary_key=True, max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    page_id = models.IntegerField(db_column='Page ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    personalization_id = models.CharField(db_column='Personalization ID', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    page_metadata_delta = models.BinaryField(db_column='Page Metadata Delta', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Profile Metadata'
        unique_together = (('profile_id', 'page_id', 'personalization_id'), ('date', 'profile_id', 'page_id', 'personalization_id'),)


class Query(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mot = models.CharField(max_length=10)
    greinarnumer = models.IntegerField()
    lina = models.IntegerField()
    grein = models.CharField(max_length=10)
    kyn = models.IntegerField()
    flokkur = models.CharField(max_length=10)
    ridill = models.IntegerField()
    numerridilsekkinotad = models.IntegerField()
    dagsetninggreinar = models.DateTimeField()
    timigreinar = models.DateTimeField()
    rasnumer = models.IntegerField()
    leitarnafn = models.CharField(max_length=30)
    ridillnumer = models.IntegerField()
    stokkkastrod = models.IntegerField()
    nafn = models.CharField(max_length=35)
    faedingarar = models.IntegerField()
    felag = models.CharField(max_length=10)
    timi = models.DecimalField(max_digits=38, decimal_places=20)
    metrar = models.DecimalField(max_digits=38, decimal_places=20)
    vindur = models.DecimalField(max_digits=38, decimal_places=20)
    arangur = models.CharField(max_length=10)
    rafmagnstimataka = models.SmallIntegerField()
    thrautarstig = models.IntegerField()
    urslitarod = models.IntegerField()
    samasaetiognaestiaundan = models.SmallIntegerField()
    nanarirod = models.IntegerField()
    stig = models.DecimalField(max_digits=38, decimal_places=20)
    stadakeppni = models.IntegerField()
    urslitarodtexti = models.CharField(max_length=10)
    iaaf_stig = models.IntegerField(db_column='IAAF Stig')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tilraun1 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur1 = models.DecimalField(max_digits=38, decimal_places=20)
    merking1 = models.IntegerField()
    tilraun2 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur2 = models.DecimalField(max_digits=38, decimal_places=20)
    merking2 = models.IntegerField()
    tilraun3 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur3 = models.DecimalField(max_digits=38, decimal_places=20)
    merking3 = models.IntegerField()
    tilraun4 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur4 = models.DecimalField(max_digits=38, decimal_places=20)
    merking4 = models.IntegerField()
    tilraun5 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur5 = models.DecimalField(max_digits=38, decimal_places=20)
    merking5 = models.IntegerField()
    tilraun6 = models.DecimalField(max_digits=38, decimal_places=20)
    vindur6 = models.DecimalField(max_digits=38, decimal_places=20)
    merking6 = models.IntegerField()
    sortorder1 = models.DecimalField(max_digits=38, decimal_places=20)
    sortorder2 = models.DecimalField(max_digits=38, decimal_places=20)
    seria = models.CharField(max_length=100)
    athugasemd = models.CharField(max_length=20)
    handvirkathugasemd = models.SmallIntegerField()
    nullarangur = models.SmallIntegerField()
    bestiaranguriar = models.DecimalField(max_digits=38, decimal_places=20)
    personulegmet = models.DecimalField(max_digits=38, decimal_places=20)
    bestiaranguriartexti = models.CharField(max_length=15)
    personulegtmettexti = models.CharField(max_length=15)
    rodiundanurslitum = models.IntegerField()
    qualification = models.CharField(max_length=1)
    gestur = models.SmallIntegerField()
    handvirkstig = models.SmallIntegerField()
    rasnumeraskyrslu = models.IntegerField()
    unglingastig = models.IntegerField(db_column='Unglingastig')  # Field name made lowercase.
    performaceremarks = models.CharField(db_column='PerformaceRemarks', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Query'


class RecordLink(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    link_id = models.AutoField(db_column='Link ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    record_id = models.BinaryField(db_column='Record ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    url1 = models.CharField(db_column='URL1', max_length=250)  # Field name made lowercase.
    url2 = models.CharField(db_column='URL2', max_length=250)  # Field name made lowercase.
    url3 = models.CharField(db_column='URL3', max_length=250)  # Field name made lowercase.
    url4 = models.CharField(db_column='URL4', max_length=250)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    note = models.BinaryField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    user_id = models.CharField(db_column='User ID', max_length=65)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    company = models.CharField(db_column='Company', max_length=30)  # Field name made lowercase.
    notify = models.SmallIntegerField(db_column='Notify')  # Field name made lowercase.
    to_user_id = models.CharField(db_column='To User ID', max_length=65)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Record Link'
        unique_together = (('record_id', 'link_id'), ('company', 'link_id'),)


class ReportList(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    menu_id = models.IntegerField(db_column='Menu ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_no_field = models.IntegerField(db_column='Line No_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    text = models.CharField(db_column='Text', max_length=30)  # Field name made lowercase.
    report_id = models.IntegerField(db_column='Report ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g_l_reports = models.IntegerField(db_column='G_L Reports')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_reports = models.IntegerField(db_column='Sales Reports')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sales_documents = models.IntegerField(db_column='Sales Documents')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    purchase_reports = models.IntegerField(db_column='Purchase Reports')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    purchase_documents = models.IntegerField(db_column='Purchase Documents')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_reports = models.IntegerField(db_column='Item Reports')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bom_reports = models.IntegerField(db_column='BOM Reports')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    resource_reports = models.IntegerField(db_column='Resource Reports')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    job_reports = models.IntegerField(db_column='Job Reports')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cont_mgt_reports = models.IntegerField(db_column='Cont_ Mgt_ Reports')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cont_mgt_documents = models.IntegerField(db_column='Cont_ Mgt_ Documents')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    employee_reports = models.IntegerField(db_column='Employee Reports')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fixed_asset_reports = models.IntegerField(db_column='Fixed Asset Reports')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Report List'
        unique_together = (('menu_id', 'line_no_field'),)


class SendToProgram(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    program_id = models.CharField(db_column='Program ID', primary_key=True, max_length=36)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    executable = models.CharField(db_column='Executable', max_length=250)  # Field name made lowercase.
    parameter = models.CharField(db_column='Parameter', max_length=250)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Send-To Program'


class Skrslur(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    mót = models.CharField(db_column='Mót', primary_key=True, max_length=10)  # Field name made lowercase.
    lína = models.IntegerField(db_column='Lína')  # Field name made lowercase.
    texti = models.CharField(db_column='Texti', max_length=30)  # Field name made lowercase.
    skýrslu_nr_field = models.IntegerField(db_column='Skýrslu nr_')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tegund_skýrslu = models.IntegerField(db_column='Tegund Skýrslu')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    virk = models.SmallIntegerField(db_column='Virk')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Skýrslur'
        unique_together = (('mót', 'lína'), ('tegund_skýrslu', 'mót', 'lína'),)


class StyleSheet(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    style_sheet_id = models.CharField(db_column='Style Sheet ID', primary_key=True, max_length=36)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_type = models.IntegerField(db_column='Object Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_id = models.IntegerField(db_column='Object ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    program_id = models.CharField(db_column='Program ID', max_length=36)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=250)  # Field name made lowercase.
    style_sheet = models.BinaryField(db_column='Style Sheet', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Style Sheet'
        unique_together = (('object_type', 'object_id', 'program_id', 'style_sheet_id'),)


class Topperformersbyyear(models.Model):
    ár = models.CharField(db_column='Ár', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rowno = models.IntegerField(db_column='RowNo', blank=True, null=True)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn', blank=True, null=True)  # Field name made lowercase.
    flokkur = models.CharField(db_column='Flokkur', max_length=10, blank=True, null=True)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10, blank=True, null=True)  # Field name made lowercase.
    arangur = models.CharField(db_column='Arangur', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vindur = models.DecimalField(db_column='Vindur', max_digits=38, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=40, blank=True, null=True)  # Field name made lowercase.
    felag = models.CharField(db_column='Felag', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dagsetning = models.DateTimeField(db_column='Dagsetning', blank=True, null=True)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=50, blank=True, null=True)  # Field name made lowercase.
    heitimots = models.CharField(db_column='HeitiMots', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aldurkeppanda = models.DecimalField(db_column='AldurKeppanda', max_digits=8, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    keppandanúmer = models.CharField(db_column='Keppandanúmer', max_length=10, blank=True, null=True)  # Field name made lowercase.
    raðsv = models.DecimalField(db_column='Raðsv', max_digits=38, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    erlrikisb = models.IntegerField(db_column='ErlRikisb', blank=True, null=True)  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár', blank=True, null=True)  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TopPerformersByYear'


class Topp10Greining(models.Model):
    rowcnt = models.IntegerField(db_column='RowCnt', blank=True, null=True)  # Field name made lowercase.
    ár = models.CharField(db_column='Ár', max_length=4, blank=True, null=True)  # Field name made lowercase.
    grein = models.CharField(db_column='Grein', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn', blank=True, null=True)  # Field name made lowercase.
    bestur = models.CharField(db_column='Bestur', max_length=40, blank=True, null=True)  # Field name made lowercase.
    félag = models.CharField(db_column='Félag', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kennitala = models.CharField(db_column='Kennitala', max_length=11, blank=True, null=True)  # Field name made lowercase.
    árangur = models.CharField(db_column='Árangur', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mt10 = models.DecimalField(db_column='MT10', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    mt10hl = models.CharField(db_column='MT10Hl', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    aldurbesta = models.IntegerField(db_column='AldurBesta', blank=True, null=True)  # Field name made lowercase.
    meðalaldurt10 = models.DecimalField(db_column='MeðalAldurT10', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    yngstur10 = models.IntegerField(db_column='Yngstur10', blank=True, null=True)  # Field name made lowercase.
    elsturt10 = models.IntegerField(db_column='ElsturT10', blank=True, null=True)  # Field name made lowercase.
    meðalaldurt3 = models.DecimalField(db_column='MeðalAldurT3', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    félögt10 = models.IntegerField(db_column='FélögT10', blank=True, null=True)  # Field name made lowercase.
    staðirt10 = models.IntegerField(db_column='StaðirT10', blank=True, null=True)  # Field name made lowercase.
    meðalvindurt10 = models.DecimalField(db_column='MeðalVindurT10', max_digits=8, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    bónus = models.CharField(db_column='Bónus', max_length=8, blank=True, null=True)  # Field name made lowercase.
    topy = models.DecimalField(db_column='TopY', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    topyhl = models.CharField(db_column='TopYHl', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meðalaldurtopy = models.DecimalField(db_column='MeðalAldurTopY', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    yngsturtopy = models.IntegerField(db_column='YngsturTopY', blank=True, null=True)  # Field name made lowercase.
    elsturtopy = models.IntegerField(db_column='ElsturTopY', blank=True, null=True)  # Field name made lowercase.
    félögtopy = models.IntegerField(db_column='FélögTopY', blank=True, null=True)  # Field name made lowercase.
    staðirtopy = models.IntegerField(db_column='StaðirTopY', blank=True, null=True)  # Field name made lowercase.
    meðalvindurtopy = models.DecimalField(db_column='MeðalVindurTopY', max_digits=8, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Topp10Greining'


class Uploadfile(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size')  # Field name made lowercase.
    contenttype = models.CharField(db_column='ContentType', max_length=200)  # Field name made lowercase.
    extension = models.CharField(db_column='Extension', max_length=10)  # Field name made lowercase.
    content = models.BinaryField(db_column='Content')  # Field name made lowercase.
    dateandtimeuploaded = models.DateTimeField(db_column='DateAndTimeUploaded', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UploadFile'


class User(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    user_id = models.CharField(db_column='User ID', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    password = models.CharField(db_column='Password', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    expiration_date = models.DateTimeField(db_column='Expiration Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'User'


class UserDefaultStyleSheet(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    user_id = models.CharField(db_column='User ID', primary_key=True, max_length=65)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_type = models.IntegerField(db_column='Object Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_id = models.IntegerField(db_column='Object ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    program_id = models.CharField(db_column='Program ID', max_length=36)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    style_sheet_id = models.CharField(db_column='Style Sheet ID', max_length=36)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'User Default Style Sheet'
        unique_together = (('user_id', 'object_type', 'object_id', 'program_id'),)


class UserGroup(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    group_id = models.CharField(db_column='Group ID', primary_key=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User Group'


class UserMenuLevel(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    id = models.CharField(db_column='ID', primary_key=True, max_length=65)  # Field name made lowercase.
    id_type = models.IntegerField(db_column='ID Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.
    object = models.BinaryField(db_column='Object', blank=True, null=True)  # Field name made lowercase.
    modified = models.DateTimeField(db_column='Modified')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User Menu Level'
        unique_together = (('id', 'id_type', 'level'),)


class UserMetadata(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    user_sid = models.CharField(db_column='User SID', primary_key=True, max_length=119)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    page_id = models.IntegerField(db_column='Page ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    personalization_id = models.CharField(db_column='Personalization ID', max_length=40)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    page_metadata_delta = models.BinaryField(db_column='Page Metadata Delta', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'User Metadata'
        unique_together = (('user_sid', 'page_id', 'personalization_id'), ('date', 'user_sid', 'page_id', 'personalization_id'),)


class UserPersonalization(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    user_sid = models.CharField(db_column='User SID', primary_key=True, max_length=119)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    profile_id = models.CharField(db_column='Profile ID', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    language_id = models.IntegerField(db_column='Language ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    company = models.CharField(db_column='Company', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User Personalization'
        unique_together = (('profile_id', 'user_sid'), ('company', 'user_sid'),)


class WebService(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    object_type = models.IntegerField(db_column='Object Type', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_name = models.CharField(db_column='Service Name', max_length=240)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_id = models.IntegerField(db_column='Object ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    published = models.SmallIntegerField(db_column='Published')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Web Service'
        unique_together = (('object_type', 'service_name'),)


class WindowsAccessControl(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    login_sid = models.CharField(db_column='Login SID', primary_key=True, max_length=119)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    role_id = models.CharField(db_column='Role ID', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    company_name = models.CharField(db_column='Company Name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Windows Access Control'
        unique_together = (('login_sid', 'role_id', 'company_name'), ('role_id', 'login_sid', 'company_name'),)


class WindowsLogin(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    sid = models.CharField(db_column='SID', primary_key=True, max_length=119)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Windows Login'


class Customers(models.Model):
    customerid = models.CharField(db_column='CustomerID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'


class jskr(models.Model):
    timestamp = models.TextField()  # This field type is a guess.
    kennitala = models.CharField(db_column='Kennitala', primary_key=True, max_length=11)  # Field name made lowercase.
    nafn = models.CharField(db_column='Nafn', max_length=31)  # Field name made lowercase.
    heimili = models.CharField(db_column='Heimili', max_length=30)  # Field name made lowercase.
    staður = models.CharField(db_column='Staður', max_length=30)  # Field name made lowercase.
    kyn = models.IntegerField(db_column='Kyn')  # Field name made lowercase.
    fæðingarár = models.IntegerField(db_column='Fæðingarár')  # Field name made lowercase.
    fjölskyldunúmer = models.CharField(db_column='Fjölskyldunúmer', max_length=11)  # Field name made lowercase.
    bannmerking = models.SmallIntegerField(db_column='Bannmerking')  # Field name made lowercase.
    íslendingur = models.SmallIntegerField(db_column='Íslendingur')  # Field name made lowercase.
    í_þjóðskrá = models.DateTimeField(db_column='Í þjóðskrá')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    látin_n_field = models.SmallIntegerField(db_column='Látin(n)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ríkisfang = models.CharField(db_column='Ríkisfang', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Þjóðskrá'
        unique_together = (('nafn', 'kennitala'), ('staður', 'heimili', 'fjölskyldunúmer', 'fæðingarár', 'kennitala'), ('fjölskyldunúmer', 'fæðingarár', 'kennitala'),)
