# Simple makefile

EXE=skim

SOURCES=$(wildcard ./src/*.cc) $(wildcard ../rapido/src/*.cc) ../NanoCORE/Nano.cc ../NanoCORE/Tools/goodrun.cc  ../NanoCORE/ElectronSelections.cc ../NanoCORE/MuonSelections.cc ../NanoCORE/Config.cc ../NanoCORE/IsolationTools.cc ../NanoCORE/MCTools.cc
SKIMMER_HEADERS=$(wildcard src/*.h)
NANOCORE_HEADERS=$(wildcard ../NanoCORE/*.h)
OBJECTS=$(SOURCES:%.cc=%.o)
SKIMMER_OBJECTS=$(patsubst ./src/%.cc,./src/%.o,$(wildcard ./src/*.cc))

CC          = g++
CXX         = g++
CXXFLAGS    = -g -O2 -Wall -fPIC -Wshadow -Woverloaded-virtual
LD          = g++
LDFLAGS     = -g -O2
SOFLAGS     = -g -shared
CXXFLAGS    = -g -O2 -Wall -fPIC -Wshadow -Woverloaded-virtual
ROOTLIBS    = $(shell root-config --libs)
ROOTCFLAGS  = $(shell root-config --cflags)
CXXFLAGS   += $(ROOTCFLAGS)
CFLAGS      = $(ROOTCFLAGS) -Wall -Wno-unused-function -g -O2 -fPIC -fno-var-tracking -DLorentzVectorPtEtaPhiM4D
#EXTRACFLAGS = -I../NanoCORE -I../rapido/src -I../NanoCORE/Tools -I${CMSSW_BASE}/../../../external/boost/1.67.0/include -I${CMSSW_BASE}/src -I../NanoTools/NanoCORE/Tools/
BOOSTFLAGS = -I ${BOOSTDIR}/include
ifeq ($(SCRAM_ARCH),el9_amd64_gcc13)
CORRECTIONLIB_DIR = /cvmfs/cms.cern.ch/el9_amd64_gcc13/external/py3-correctionlib/2.7.0-65928cbe29548b423e729eb9829fee69/lib/python3.9/site-packages/correctionlib
else ifeq ($(SCRAM_ARCH),el8_amd64_gcc12)
CORRECTIONLIB_DIR = /cvmfs/cms.cern.ch/el8_amd64_gcc12/external/py3-correctionlib/2.5.0-ce7c6d001f4fb02448d4b37a11622e58/lib/python3.9/site-packages/correctionlib
else
$(error Unsupported SCRAM_ARCH=$(SCRAM_ARCH). Set up el8 or el9 environment first.)
endif
CORRECTIONLIB_CFLAGS = -I$(CORRECTIONLIB_DIR)/include
CORRECTIONLIB_LIBS = -L$(CORRECTIONLIB_DIR)/lib -lcorrectionlib -Wl,-rpath,$(CORRECTIONLIB_DIR)/lib
EXTRACFLAGS = -I../NanoCORE -I../rapido/src -I../NanoCORE/Tools -I${CMSSW_BASE}/src -I../NanoTools/NanoCORE/Tools/ $(CORRECTIONLIB_CFLAGS)

EXTRAFLAGS  = -fPIC -ITMultiDrawTreePlayer -Wunused-variable -lTMVA -lEG -lGenVector -lXMLIO -lMLP -lTreePlayer $(CORRECTIONLIB_LIBS)

all: $(EXE)

$(EXE): $(OBJECTS)
	$(LD) $(CXXFLAGS) $(LDFLAGS) $(OBJECTS) $(ROOTLIBS) $(BOOSTFLAGS) $(EXTRAFLAGS) -o $@

# Skimmer objects depend on skimmer + NanoCORE headers
$(SKIMMER_OBJECTS): $(SKIMMER_HEADERS) $(NANOCORE_HEADERS)

%.o: %.cc
	$(CC) $(CFLAGS) $(EXTRACFLAGS) -c $< -o $@

.DELETE_ON_ERROR:

clean:
	rm -f main.o $(EXE) $(wildcard ./src/*.o)

cleanall:
	rm -f $(OBJECTS) $(EXE)
	rm -f ../NanoCORE/*.o ../NanoCORE/Tools/*.o ../rapido/src/*.o
