<script runat="server">
  protected override void OnLoad(EventArgs e)
  {
      Response.Redirect("https://sif.fri.is/keppandi/" + Request.QueryString["CompetitorCode"]);
  }
</script>
