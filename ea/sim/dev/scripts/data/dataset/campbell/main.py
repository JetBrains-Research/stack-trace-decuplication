import argparse
from pathlib import Path

from ea.sim.dev.scripts.data.dataset.common.config import DatasetConfig, SegmentsConfig, Paths
from ea.sim.dev.scripts.data.dataset.common.templates.template_1 import parse
from ea.sim.main.data.buckets.bucket_data import DataSegment
from ea.sim.main.utils import Scope

CONFIG = DatasetConfig(
    name=Scope.Campbell.value,
    random_seed=42,
    segments=SegmentsConfig(
        train=DataSegment(0, 1571),
        val=DataSegment(1571, 126),
        test=DataSegment(1698, 1370),
    ),
    scope=Scope.Campbell
)

def main(paths: Paths):
    parse(CONFIG, paths)


if __name__ == "__main__":
    _parser = argparse.ArgumentParser()
    _parser.add_argument("--reports_dir", type=Path)
    _parser.add_argument("--state_path", type=Path)
    _parser.add_argument("--d", type=Path)
    _args = _parser.parse_args()
    _paths = Paths(
        reports_dir=_args.reports_dir,
        state_path=_args.state_path,
        save_dir=_args.save_dir
    )

    main(_paths)
