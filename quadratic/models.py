from django.db import models

class ResultsCalc(models.Model):
    result_text = models.CharField(max_length=200)

    def __unicode__(self):
    	return self.result_text

class ReportAnError(models.Model):
    report_text = models.CharField(max_length=200)
    
    def __unicode__(self):
    	return self.report_text