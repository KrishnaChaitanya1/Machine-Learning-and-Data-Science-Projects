class ValueCounts:

    def __init__(self, columns):
        self.columns = columns

    def valcounts_multiple_cat_cols(self):
        """
        Returns value counts for multiple
        """        
        for col in columns:
            col.value_counts()
