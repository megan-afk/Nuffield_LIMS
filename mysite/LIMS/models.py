from django.db import models
# Create your models here.
class Sample(models.Model):
    sample_name = models.CharField(max_length=200, unique=True)
    taxon_id = models.CharField(max_length=20)
    scientific_name = models.CharField(max_length=200)
    common_name = models.CharField(max_length=200, default='')
    date_collected = models.DateTimeField("date collected")
    Sample_Img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.sample_name

class Extraction(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    extraction_date = models.DateTimeField("date extracted")
    extraction_name = models.CharField(max_length=200)
    extraction_method_list = ["phenol chloroform", "ethanol precipitation", "silica"]
    extraction_method_list_sorted = sorted([(item, item) for item in extraction_method_list])
    extraction_method = models.CharField(max_length=25, choices=extraction_method_list_sorted, default="ethanol precipitation")


class QC(models.Model):
    extraction = models.ForeignKey(Extraction, on_delete=models.CASCADE, default="")
    quality_distribution = models.FloatField(default=0)
    ambiguous_base_content = models.FloatField(default=0)
    passQC = models.BooleanField(default=False)


class Sequencing(models.Model):
    extraction = models.ForeignKey(Extraction, on_delete=models.CASCADE, default="")
    sequencing_date = models.DateTimeField("date sequenced")
    mean_read_length = models.FloatField(default=0)
    file_name = models.CharField(max_length=200)
    sequencing_method_list = ["illuming", "pacbio", "oxford namopore"]
    sequencing_method_list_sorted = sorted([(item, item) for item in sequencing_method_list])
    sequencing_method = models.CharField(max_length=25, choices=sequencing_method_list_sorted, default="illuming")


