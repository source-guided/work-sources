"""원천 소유의 대표 독자 질문으로 실제 참조 검색과 후속 주소 해석을 검증한다."""

from pathlib import Path
import tempfile
import unittest

from reference_catalog import Catalog
from reference_io import load_index
from reference_workflow import Workflow, ROOT as CLIENT_PLUGIN
from source_connections import Connections

ROOT = Path(__file__).resolve().parents[1]
CASES = [
    ('작업 재개', 'context-workflow'),
    ('resume', 'context-workflow'),
    ('검증', 'verification-workflow'),
    ('verification', 'verification-workflow'),
    ('증거', 'evidence'),
    ('evidence', 'evidence'),
    ('독립 검토', 'independent-review'),
    ('independent review', 'independent-review'),
]


class DiscoveryTest(unittest.TestCase):
    def test_connected_root_reads_each_owner_through_discovered_area(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "connections.json"
            trace = Path(tmp) / "trace.jsonl"
            connections = Connections(state)
            connections.select("work", "custom", index=str(ROOT / "references/index.json"))
            flow = Workflow(trace)
            flow.read(CLIENT_PLUGIN / "references/governance/index.json", "routing-policy")
            for query, identifier, area in [("작업 재개", "context-workflow", "context"), ("검증", "verification-workflow", "verification")]:
                with self.subTest(area=area):
                    found = connections.discover("work", query)
                    reference = next(item["reference"] for item in found["references"] if item["reference"]["id"] == identifier)
                    self.assertEqual(Path(reference["index"]), ROOT / "references" / area / "index.json")
                    read = connections.access("work", trace, identifier=identifier, reference_index=reference["index"], reference_access=reference["access"])
                    self.assertTrue(Path(read["reference"]["resolved"]["address"]).is_relative_to(ROOT / "capabilities" / area))
                    self.assertTrue(read["content"].strip())
            self.assertEqual(flow.audit()["read"], 3)

    def test_reader_questions_find_relevant_sources(self):
        catalog = Catalog(load_index)
        for query, identifier in CASES:
            with self.subTest(query=query):
                found = catalog.discover([ROOT / "references/index.json"], query, limit=5)
                self.assertTrue(found["complete"], found["errors"])
                matches = [item for item in found["references"] if item["reference"]["id"] == identifier]
                self.assertTrue(matches, f"{query!r} did not find {identifier!r} in the first five results")
                reference = matches[0]["reference"]
                resolved = catalog.resolve(reference["index"], identifier, access=reference["access"])
                self.assertEqual(resolved["address"], matches[0]["address"])
                self.assertTrue(Path(resolved["address"]).is_relative_to(ROOT))
                self.assertTrue(Path(resolved["address"]).is_file())

    def test_unrelated_query_does_not_claim_a_match(self):
        found = Catalog(load_index).discover([ROOT / "references/index.json"], "zzunrelated731zz")
        self.assertTrue(found["complete"])
        self.assertEqual(found["references"], [])


if __name__ == "__main__":
    unittest.main()
