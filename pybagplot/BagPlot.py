#!/usr/bin/env python3
"""Contains the main package functionality."""

from __future__ import annotations

import pandas as pd


class PlotBagTest:
    """Reading Data from Greg's BAG Test csv file and plot the columns vs time(s)."""

    def __init__(self: PlotBagTest, filen: str, title: str) -> None:
        """Execute loadfile functionality."""
        self.filen = filen
        self.title = title
        self.head = [
            "millis",
            "mSLPM",
            "umH2O",
            "cpuLoad",
            "position",
            "temperature",
            "direction",
            "pwmSpeed",
            "analogRead",
        ]

    def loadfile(self: PlotBagTest) -> None:
        """Execute loadfile functionality."""
        df = pd.read_csv(self.filen, skiprows=10, header=None, names=self.head)
        df.index = (df.iloc[:, 0] - df.iloc[0, 0]) / 1000
        df.index.name = "sec"
        return df

    def run(self: PlotBagTest) -> None:
        """Execute run functionality."""
        df = self.loadfile()
        df.plot(figsize=(10, 12), subplots=True, grid=True, title=self.title)
