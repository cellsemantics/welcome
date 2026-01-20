# Welcome

A small starter repository for the cellsemantics organization — a friendly place to keep onboarding materials, demos, and quick example projects. This README provides an easy-to-follow overview, quick start instructions, and guidance for contributors.

## Overview

This repository is intended to:
- Serve as a "welcome" or landing repo for new contributors and team members.
- Contain examples, documentation, and links to other projects in the organization.
- Provide a lightweight starter template for small demos or experiments.

## Features

- Minimal, easy-to-read structure
- Example files and templates for docs, issues, and PRs
- Guidance for onboarding and contributing
- **Bucket Sort Implementation**: Production-ready bucket sort algorithm in Python with comprehensive tests

## Quick start

1. Clone the repository
   ```bash
   git clone https://github.com/cellsemantics/welcome.git
   cd welcome
   ```

2. Inspect the repository structure and example files:
   - README.md — this file
   - bucket_sort.py — comprehensive bucket sort implementation
   - test_bucket_sort.py — unit tests for bucket sort
   - BUCKET_SORT_README.md — detailed bucket sort documentation
   - requirements.txt — Python dependencies
   - docs/ — optional documentation and onboarding guides
   - examples/ — demo projects or sample code
   - .github/ — issue and PR templates, workflows

3. Make changes locally, then push and open a pull request:
   ```bash
   git checkout -b my-update
   # edit files
   git add .
   git commit -m "Improve welcome docs"
   git push origin my-update
   # Create a PR on GitHub
   ```

## Bucket Sort Algorithm

This repository includes a comprehensive bucket sort implementation in Python. Bucket sort is a distribution-based sorting algorithm that achieves O(n + k) average time complexity.

### Quick Example

```python
from bucket_sort import bucket_sort

# Sort integers
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bucket_sort(numbers)
print(sorted_numbers)  # [11, 12, 22, 25, 34, 64, 90]

# Sort floats
decimals = [0.42, 0.32, 0.23, 0.52, 0.25]
sorted_decimals = bucket_sort(decimals)
```

For complete documentation, examples, and API reference, see [BUCKET_SORT_README.md](BUCKET_SORT_README.md).

### Running Tests

```bash
# Run the test suite
python test_bucket_sort.py

# Or run the example demonstrations
python bucket_sort.py
```

## Usage

Customize this repo for your needs:
- Add an onboarding checklist in `docs/`
- Place short code samples in `examples/`
- Update `CONTRIBUTING.md` with org-specific guidelines

## Development

- Keep commits small and focused.
- Use descriptive PR titles and reference any relevant issue numbers.
- If you add CI workflows, keep jobs fast and focused on the essentials for this repo.

## Contributing

Contributions are welcome. Typical contributions include:
- Improving documentation
- Adding small example projects
- Adding or updating templates in `.github/`

Please follow the contribution guidelines:
1. Fork the repo and create a branch for your change.
2. Open a PR describing the change and why it's useful.
3. Be responsive to review feedback.

## License

This repository is provided under the MIT License. See [LICENSE](LICENSE) for details.

## Contact / Support

If you need help or want to discuss improvements, open an issue or reach out to the maintainers via GitHub discussions or direct mention in the repo.