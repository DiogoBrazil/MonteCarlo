class StatsCalculator:
    @staticmethod
    def calculate_averages(stats_list):
        totals = {}
        count = len(stats_list)

        for stats in stats_list:
            for key, value in stats.items():
                if key in totals:
                    totals[key] += value
                else:
                    totals[key] = value

        averages = {key: value / count for key, value in totals.items()}
        return averages
