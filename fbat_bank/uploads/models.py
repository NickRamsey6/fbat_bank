from django.db import models

# Create your models here.
class Statement(models.Model):
    """A bank account statement"""
    # text = models.CharField(max_length=200)
    # date_added = models.DateTimeField(auto_now_add=True)
    transaction_date = models.CharField(max_length=50, default=None)
    post_date = models.CharField(max_length=50, default=None)
    description = models.TextField(default=None)
    category = models.CharField(max_length=50, default=None)
    type = models.CharField(max_length=50, default=None)
    amount = models.CharField(max_length=50, default=None)
    


    def __str__(self):
        """Return a string representation of the model"""
        return self.transaction_date

# class Transaction(models.Model):
#      """a specific transaction from a specific statement"""
#      statement = models.ForeignKey(
#          'Statement',
#          on_delete=models.DO_NOTHING
#          )
#      text = models.TextField()
#      date_added = models.DateTimeField(auto_now_add=True)

#      class Meta:
#          verbose_name_plural = 'transactions'

#      def __str__(self):
#         """Return a string representation of the model"""
#         return self.text[:50] + "..."
