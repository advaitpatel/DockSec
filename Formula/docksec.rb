class Docksec < Formula
    include Language::Python::Virtualenv
  
    desc "AI-Powered Docker Security Analyzer"
    homepage "https://github.com/advaitpatel/DockSec"
    url "https://files.pythonhosted.org/packages/source/d/docksec/docksec-0.1.0.tar.gz"
    sha256 "0649aee5d750f21308d9f902f1bd0522589f0ea94a5d64ec58bcff126e7be293"
    license "MIT"
  
    depends_on "python@3.12"
  
    resource "langchain" do
      url "https://files.pythonhosted.org/packages/fc/f9/a256609096a9fc7a1b3a6300a97000091efabdf21555a97988f93d4d9258/langchain-0.3.25.tar.gz"
      sha256 "a1d72aa39546a23db08492d7228464af35c9ee83379945535ceef877340d2a3a"
    end
  
    resource "langchain-openai" do
      url "https://files.pythonhosted.org/packages/53/fb/536562278d932c80e6a7143f46f14cc3006c0828d77c4cb6a69be112519c/langchain_openai-0.3.16.tar.gz"
      sha256 "4e423e39d072f1432adc9430f2905fe635cc019f01ad1bdffa5ed8d0dda32149"
    end
  
    resource "python-dotenv" do
      url "https://files.pythonhosted.org/packages/88/2c/7bb1416c5620485aa793f2de31d3df393d3686aa8a8506d11e10e13c5baf/python_dotenv-1.1.0.tar.gz"
      sha256 "41f90bc6f5f177fb41f53e87666db362025010eb28f60a01c9143bfa33a2b2d5"
    end
  
    resource "pandas" do
      url "https://files.pythonhosted.org/packages/9c/d6/9f8431bacc2e19dca897724cd097b1bb224a6ad5433784a44b587c7c13af/pandas-2.2.3.tar.gz"
      sha256 "4f18ba62b61d7e192368b84517265a99b4d7ee8912f8708660fb4a366cc82667"
    end
  
    resource "tqdm" do
      url "https://files.pythonhosted.org/packages/a8/4b/29b4ef32e036bb34e4ab51796dd745cdba7ed47ad142a9f4a1eb8e0c744d/tqdm-4.67.1.tar.gz"
      sha256 "f8aef9c52c08c13a65f30ea34f4e5aac3fd1a34959879d7e59e63027286627f2"
    end
  
    resource "colorama" do
      url "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz"
      sha256 "08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"
    end
  
    resource "rich" do
      url "https://files.pythonhosted.org/packages/a1/53/830aa4c3066a8ab0ae9a9955976fb770fe9c6102117c8ec4ab3ea62d89e8/rich-14.0.0.tar.gz"
      sha256 "82f1bc23a6a21ebca4ae0c45af9bdbc492ed20231dcb63f297d6d1021a9d5725"
    end
  
    resource "fpdf" do
      url "https://files.pythonhosted.org/packages/37/c6/608a9e6c172bf9124aa687ec8b9f0e8e5d697d59a5f4fad0e2d5ec2a7556/fpdf-1.7.2.tar.gz"
      sha256 "125840783289e7d12552b1e86ab692c37322e7a65b96a99e0ea86cca041b6779"
    end
  
    def install
      virtualenv_install_with_resources
    end
  
    test do
      system "#{bin}/docksec", "--help"
    end
  end