class ValueCounts:

    def __init__(self, columns, df):
        self.columns = columns
        self.df = df

    def valcounts_multiple_cat_cols(self):
        """
        Returns value counts for multiple.

        :param columns: Categorical columns dataframe
        :type columns: DataFrame
        :param df: Main DataFrame
        :type df: DataFrame

        :return None:
        """

        assert len(self.columns) != 0

        for col in self.columns:
            print(f"Value Counts for {col}")
            print("\n")
            print(self.df[col].value_counts())
            print("---------------------")
        