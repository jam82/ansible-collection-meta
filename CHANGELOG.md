# CHANGELOG



## v0.3.0 (2024-03-19)

### Chore

* chore: update version control configuration and settings

- Update commitizen version from `v3.15.0` to `v3.20.0` in `.pre-commit-config.yaml`
- Remove `version_provider` and `tag_format` settings in `pyproject.toml`
- Update the `version_variables` in `pyproject.toml` to include `galaxy.yml:version`

Signed-off-by: Jonas Mauer &lt;jam@kabelmail.net&gt; ([`4ea5017`](https://github.com/jomrr/ansible-collection-dev/commit/4ea501779ee5872e6ec4676beb030536681d57a3))

### Feature

* feat: add to_lintable_yaml filter because default ansible filters produce non-ansible-lintable output... (◔_◔) ([`9a5803a`](https://github.com/jomrr/ansible-collection-dev/commit/9a5803a59ea3f7ea43fc3f66092038fa024d624e))

### Fix

* fix: disable tags due to overlaps with hostname ([`7ada8e0`](https://github.com/jomrr/ansible-collection-dev/commit/7ada8e08921b9c4f2bc770d685e62c67085e688e))


## v0.2.2 (2024-02-20)

### Build

* build(release): version 0.2.2 ([`cc8ae30`](https://github.com/jomrr/ansible-collection-dev/commit/cc8ae30fcb259535c82df32d35bafda9558e12f5))

### Fix

* fix: Update version variable in pyproject.toml ([`e8e0526`](https://github.com/jomrr/ansible-collection-dev/commit/e8e05260860f5c5b81f4213446784de7eaabe16e))


## v0.2.1 (2024-02-20)

### Build

* build(release): version 0.2.1 ([`4d7cfae`](https://github.com/jomrr/ansible-collection-dev/commit/4d7cfaeb1be5cd21efce58721b8cb62ba71a544f))

### Fix

* fix: version 1.0.0 linting issue and include galaxy.yml in version files ([`f49e75f`](https://github.com/jomrr/ansible-collection-dev/commit/f49e75f511810c93feecb0e3a100b053017e5280))


## v0.2.0 (2024-02-20)

### Build

* build(release): version 0.2.0 ([`0e013b8`](https://github.com/jomrr/ansible-collection-dev/commit/0e013b82badb7a31503324fb636c81683bdd497e))

### Documentation

* docs: update README with fetch_github_repos module and github_versions lookup plugin ([`a9dd72d`](https://github.com/jomrr/ansible-collection-dev/commit/a9dd72d444bd594b8f3540b487ec582a8d4ed496))

### Feature

* feat: Add fetch_github_repos module for fetching and caching GitHub repository data. ([`7579ef6`](https://github.com/jomrr/ansible-collection-dev/commit/7579ef6497fc8fc7d479bc59fcf458a2a33af59b))

* feat: Add GitHub version lookup plugin ([`4046f26`](https://github.com/jomrr/ansible-collection-dev/commit/4046f26f04e9d90560ff9487607dfe650e74d558))


## v0.1.1 (2024-02-20)

### Build

* build(release): version 0.1.1 ([`a59d44d`](https://github.com/jomrr/ansible-collection-dev/commit/a59d44d63e5dfc005795ea97ebf92395d70b829d))

### Fix

* fix: Use FQCNs in test_generate_argument_spec.yml ([`2e42e3a`](https://github.com/jomrr/ansible-collection-dev/commit/2e42e3a0aef8dbfa11d3500c82060758adcabd85))

### Refactor

* refactor: Remove playbooks and templates, adopt README ([`e7ae838`](https://github.com/jomrr/ansible-collection-dev/commit/e7ae838887a1b91da536de1632e5237618be5c70))

### Style

* style: Update GitHub URL in LICENSE file ([`88fa8e1`](https://github.com/jomrr/ansible-collection-dev/commit/88fa8e15a0b8814895fe1fd3d6bf2d2f485224ef))


## v0.1.0 (2024-02-19)

### Build

* build(release): version 0.1.0 ([`64dba7a`](https://github.com/jomrr/ansible-collection-dev/commit/64dba7a9dcba10f2a2fcc6f5871523a671d08651))

* build: add pre-commit-config and pyproject.toml ([`f4aa4ab`](https://github.com/jomrr/ansible-collection-dev/commit/f4aa4ab6d1dc50d4655315760ce9d65de3a378cb))

* build: rename and delte changelog &gt; auto generated ([`0c43f14`](https://github.com/jomrr/ansible-collection-dev/commit/0c43f147624650c195e70f12d90ffa2e9beec5c3))

### Feature

* feat: add references ([`037f463`](https://github.com/jomrr/ansible-collection-dev/commit/037f463099f026d7922bae859e6cd2914e56d9c6))

* feat: deprecate platforms list in meta/main.yml ([`867786b`](https://github.com/jomrr/ansible-collection-dev/commit/867786bd98440290b632e486df42e0ce2aec22a9))

* feat: simplify meta_platforms dict ([`a10b67e`](https://github.com/jomrr/ansible-collection-dev/commit/a10b67e8281dba17a3090b52d4521e8317a07315))

* feat: combine platform info in meta_platforms ([`d905c98`](https://github.com/jomrr/ansible-collection-dev/commit/d905c98a7d6cb61720f9fad440afdf23324fe158))

* feat: add playbooks and templates for generating docs ([`f41db01`](https://github.com/jomrr/ansible-collection-dev/commit/f41db01bb76373befcfcf445a1a2841ab240b052))

* feat: add remove playbook ([`a3d87bc`](https://github.com/jomrr/ansible-collection-dev/commit/a3d87bcb0559e02f35da5053f426a4c6c3c35fe8))

* feat: add playbook and template for meta/main.yml ([`37ac9c0`](https://github.com/jomrr/ansible-collection-dev/commit/37ac9c006427da2975420bd86b88ed122a2fce71))

* feat: group hosts by galaxy_tags ([`72c1153`](https://github.com/jomrr/ansible-collection-dev/commit/72c11536865564e2a90450ea24255efb861bee4d))

* feat: first commit ([`9896dc5`](https://github.com/jomrr/ansible-collection-dev/commit/9896dc58497c113b87010eab52860dbb3576a3a7))

* feat: first commit ([`f9338d7`](https://github.com/jomrr/ansible-collection-dev/commit/f9338d77a296b9ee7a41ffa0df5625e8cadb84ff))

### Fix

* fix: template logic and line breaks ([`62f3736`](https://github.com/jomrr/ansible-collection-dev/commit/62f3736ebf129a468157e35fc768e2a589949fd7))

* fix: var naming ([`6089556`](https://github.com/jomrr/ansible-collection-dev/commit/6089556e41f9574ae20727201dd256f53aa7f834))

* fix: update toc ([`66d0b02`](https://github.com/jomrr/ansible-collection-dev/commit/66d0b02492a8aafc0650b59c1435df9b27d5905e))

* fix: missing endif and defaults reference ([`6f8f09d`](https://github.com/jomrr/ansible-collection-dev/commit/6f8f09dfbd97e3143f4e71500e196aa805f5b52b))

* fix: docker hub link ([`ca245a0`](https://github.com/jomrr/ansible-collection-dev/commit/ca245a0abadef667ee802d2be74bca84c1689e8b))

* fix: chroot ([`d4db0d4`](https://github.com/jomrr/ansible-collection-dev/commit/d4db0d492dcc9eb08984aad18f7e36d9840e6b83))

* fix: use remote_addr ([`9ab9fb7`](https://github.com/jomrr/ansible-collection-dev/commit/9ab9fb72a3c6d0097a2bd46d3da869a57fbdffaa))

### Refactor

* refactor: move templates to sub directory ([`753061b`](https://github.com/jomrr/ansible-collection-dev/commit/753061b2664fa436db8c80c91770ae73ff788c88))

* refactor(playbooks): split docs.yml in separate plays ([`5eba169`](https://github.com/jomrr/ansible-collection-dev/commit/5eba1696c12eddc24ad3f1831ac5f88d8c6daf21))

* refactor: inventory name, playbooks, templates ([`03e5463`](https://github.com/jomrr/ansible-collection-dev/commit/03e54630ccdc86f0b7b00b0259b12f15b4865f8a))

### Style

* style: contributing code block ([`1a95f7a`](https://github.com/jomrr/ansible-collection-dev/commit/1a95f7a12618073f0d91bf48663bdf133afaff98))

* style: explicit become: false ([`4cf9966`](https://github.com/jomrr/ansible-collection-dev/commit/4cf9966bacb10be5c62a807a89dd368c5dd804ba))

* style: restructure .gitignore ([`a3e3ca2`](https://github.com/jomrr/ansible-collection-dev/commit/a3e3ca2cc0aa90a8f7c3db2d76ba43440701f3e6))

### Unknown

* doc(README): adjust description ([`ca1a04e`](https://github.com/jomrr/ansible-collection-dev/commit/ca1a04ea5579a6d47e388ccea0f7a736d80f1105))
