#!/usr/bin/env python3
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Skill and Agent Schema Test Suite for bean-roaster.
Validates SKILL.md files, copy-editor.md agent schema, rules files, and absence of deprecated files.
"""

import os
import unittest
import yaml


def find_repo_root():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(script_dir, ".."))


def parse_frontmatter(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        raise ValueError(f"{path} does not start with YAML frontmatter delimiter '---'")
    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{path} frontmatter delimiter '---' is not closed")
    return yaml.safe_load(parts[1]), parts[2]


class TestSkillsSchema(unittest.TestCase):

    def setUp(self):
        self.repo_root = find_repo_root()
        self.skills_dir = os.path.join(self.repo_root, "skills")
        self.agents_dir = os.path.join(self.repo_root, "agents")
        self.rules_dir = os.path.join(self.repo_root, "rules")

    def test_expected_skills_exist(self):
        expected = {"cupping-form", "domain-modeling", "grill", "ideator", "write-prd"}
        actual = {
            d for d in os.listdir(self.skills_dir)
            if os.path.isdir(os.path.join(self.skills_dir, d)) and not d.startswith(".")
        }
        self.assertEqual(actual, expected)

    def test_all_skills_have_skill_md_and_valid_frontmatter(self):
        skill_folders = [
            d for d in os.listdir(self.skills_dir)
            if os.path.isdir(os.path.join(self.skills_dir, d)) and not d.startswith(".")
        ]
        for skill_name in sorted(skill_folders):
            skill_md_path = os.path.join(self.skills_dir, skill_name, "SKILL.md")
            with self.subTest(skill=skill_name):
                self.assertTrue(os.path.exists(skill_md_path))
                data, body = parse_frontmatter(skill_md_path)
                self.assertIsInstance(data, dict)
                self.assertEqual(data.get("name"), skill_name)
                self.assertTrue(data.get("description"))
                for forbidden in ("visual-dashboard.html", "manage_dashboard.py", "bean-to-cup", "visual-glossary.html"):
                    self.assertNotIn(forbidden, body, f"Forbidden reference {forbidden} in {skill_md_path}")

    def test_copy_editor_agent_schema(self):
        agent_path = os.path.join(self.agents_dir, "copy-editor.md")
        self.assertTrue(os.path.exists(agent_path))
        data, _ = parse_frontmatter(agent_path)
        self.assertEqual(data.get("name"), "copy-editor")
        self.assertEqual(data.get("kind"), "local")
        self.assertIs(data.get("subagent"), True)
        self.assertIs(data.get("mainAgent"), False)
        self.assertEqual(data.get("model"), "inherit")
        self.assertEqual(data.get("tools"), ["read_file", "write_file", "edit_file"])

    def test_removed_files_absent(self):
        removed_paths = [
            "agents/threat-modeler.md",
            "skills/feature",
            "skills/grilling",
            "skills/domain-modeling/resources/visual-glossary.html",
            "scripts/sync_dashboard_if_available.py",
            "rules/gh.md",
            "gemini-extension.json",
        ]
        for rel in removed_paths:
            full_path = os.path.join(self.repo_root, rel)
            self.assertFalse(os.path.exists(full_path), f"Deprecated path should be removed: {rel}")

    def test_rules_plain_markdown(self):
        for rule_file in ("AGENTS.md", "general.md"):
            rule_path = os.path.join(self.rules_dir, rule_file)
            self.assertTrue(os.path.exists(rule_path), f"Missing rule file: {rule_file}")
            with open(rule_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertFalse(content.startswith("---"), f"{rule_file} must not have YAML frontmatter")
            self.assertNotIn("visual-dashboard.html", content)


if __name__ == "__main__":
    unittest.main()
