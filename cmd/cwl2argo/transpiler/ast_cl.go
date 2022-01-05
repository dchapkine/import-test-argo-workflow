// ________________________________________________________________________________
//
// Abstract Syntax Tree
//
// The AST for CWL  is represented in `ast_cl.go`
// Note that a few modifications have been made to
// the AST to make it more convenient to represent in Golang.
//
// Sum Types
//
// Sum Types (types of the form "ty | []ty") are represented by interfaces,
// some extra type safety has been added by requiring the implementation of a dummy method in order to satisfy the interface.
//
// Normalisation
//
// Note how maps are not present in the AST
// maps are to be represented by arrays.
// This may incur a small performance hit for large arrays where lookup is required (but generally shouldn't since we will be traversing the entire data structure usually).
//
// Note how sum types of the form "ty | []ty" are represented in the AST.
// This form is generally normalised to simply be "[]ty", the distinction between "ty | []ty" is made by examining the
// length of the array.
package transpiler

type CWLRequirements interface {
	isCWLRequirement()
}

type DockerRequirement struct {
	Class                 string // constant DockerRequirement
	DockerPull            *string
	DockerLoad            *string
	DockerFile            *string
	DockerImport          *string
	DockerImageId         *string
	DockerOutputDirectory *string
}

type SoftwarePackage struct {
	Package string
	Version []string
	Specs   []string
}

type SoftwareRequirement struct {
	Class    string // constant SoftwareRequirement
	Packages []SoftwarePackage
}

type LoadListingRequirement struct {
	Class       string // constant LoadListingRequirement
	LoadListing LoadListingEnum
}

type Dirent struct {
	entry     CWLExpressionString
	entryName CWLExpressionString
	writeable *bool
}

type InitialWorkDirRequirementListing interface {
	isInitialWorkDirRequirementListing()
}

type InitialWorkDirRequirement struct {
	Class   string // constant InitialWorkDirRequirement
	Listing InitialWorkDirRequirementListing
}

type InlineJavascriptRequirement struct {
	Class         string // constant InlineJavascriptRequirement
	ExpressionLib []string
}

type SchemaDefRequirementType interface {
	isSchemaDefRequirementType()
}

type SchemaDefRequirement struct {
	Class string // constant SchemaDefRequirement
	Types []SchemaDefRequirementType
}

type EnvironmentDef struct {
	EnvName  string
	EnvValue CWLExpressionString
}

type EnvVarRequirement struct {
	Class  string // constant EnvVarRequirement
	EnvDef []EnvironmentDef
}

type ShellCommandRequirement struct {
	Class string // constant ShellCommandRequirement
}

type WorkReuse struct {
	Class       string // constant WorkReuse
	enableReuse CWLExpressionBool
}

type NetworkAccess struct {
	Class         string // constant NetworkAccess
	NetworkAccess CWLExpressionBool
}

type InplaceUpdateRequirement struct {
	Class         string // constant InplaceUpdateRequirement
	InplaceUpdate Bool
}

type ToolTimeLimit struct {
	Class     string // constant ToolTimeLimit
	TimeLimit CWLExpressionInt
}

type ResourceRequirement struct {
	Class     string // constand ResourceRequirement
	CoresMin  *CWLExpressionNum
	CoresMax  *CWLExpressionNum
	RamMin    *CWLExpressionNum
	RamMax    *CWLExpressionNum
	TmpDirMin *CWLExpressionNum
	TmpDirMax *CWLExpressionNum
	OutdirMin *CWLExpressionNum
	OutdirMax *CWLExpressionNum
}

func (_ InlineJavascriptRequirement) isCWLRequirement() {}
func (_ SchemaDefRequirement) isCWLRequirement()        {}
func (_ LoadListingRequirement) isCWLRequirement()      {}
func (_ DockerRequirement) isCWLRequirement()           {}
func (_ SoftwareRequirement) isCWLRequirement()         {}
func (_ InitialWorkDirRequirement) isCWLRequirement()   {}
func (_ EnvVarRequirement) isCWLRequirement()           {}
func (_ ShellCommandRequirement) isCWLRequirement()     {}
func (_ WorkReuse) isCWLRequirement()                   {}
func (_ NetworkAccess) isCWLRequirement()               {}
func (_ InplaceUpdateRequirement) isCWLRequirement()    {}
func (_ ToolTimeLimit) isCWLRequirement()               {}

func (_ CommandlineInputRecordSchema) isSchemaDefRequirementType() {}
func (_ CommandlineInputEnumSchema) isSchemaDefRequirementType()   {}
func (_ CommandlineInputArraySchema) isSchemaDefRequirementType()  {}
func (_ DockerRequirement) isSchemaDefRequirementType()            {}
func (_ SoftwareRequirement) isSchemaDefRequirementType()          {}
func (_ InitialWorkDirRequirement) isSchemaDefRequirementType()    {}

type CommandlineInputRecordFieldType interface {
	isCommandlineInputRecordFieldType()
}

func (_ CWLNull) isCommandlineInputRecordFieldType()                      {}
func (_ CWLBool) isCommandlineInputRecordFieldType()                      {}
func (_ CWLInt) isCommandlineInputRecordFieldType()                       {}
func (_ CWLLong) isCommandlineInputRecordFieldType()                      {}
func (_ CWLFloat) isCommandlineInputRecordFieldType()                     {}
func (_ CWLDouble) isCommandlineInputRecordFieldType()                    {}
func (_ CWLString) isCommandlineInputRecordFieldType()                    {}
func (_ CWLFile) isCommandlineInputRecordFieldType()                      {}
func (_ CWLDirectory) isCommandlineInputRecordFieldType()                 {}
func (_ CommandlineInputRecordSchema) isCommandlineInputRecordFieldType() {}
func (_ CommandlineInputArraySchema) isCommandlineInputRecordFieldType()  {}
func (_ CommandlineInputEnumSchema) isCommandlineInputRecordFieldType()   {}

type CommandlineInputRecordField struct {
	Name           string
	Type           []CommandlineInputRecordFieldType // len(1) represents scalar len > 1 represents array
	Doc            []string
	Label          *string
	SecondaryFiles []CWLSecondaryFileSchema
	Streamable     *bool
	Format         CWLFormat
	LoadContents   *bool
	LoadListing    LoadListingEnum
	InputBinding   *CommandlineBinding
}

type CommandlineInputArraySchemaType interface {
	isCommandlineInputArraySchemaType()
}

func (_ CWLNull) isCommandlineInputArraySchemaType()                      {}
func (_ CWLBool) isCommandlineInputArraySchemaType()                      {}
func (_ CWLInt) isCommandlineInputArraySchemaType()                       {}
func (_ CWLLong) isCommandlineInputArraySchemaType()                      {}
func (_ CWLFloat) isCommandlineInputArraySchemaType()                     {}
func (_ CWLDouble) isCommandlineInputArraySchemaType()                    {}
func (_ CWLString) isCommandlineInputArraySchemaType()                    {}
func (_ CWLFile) isCommandlineInputArraySchemaType()                      {}
func (_ CWLDirectory) isCommandlineInputArraySchemaType()                 {}
func (_ CommandlineInputRecordSchema) isCommandlineInputArraySchemaType() {}
func (_ CommandlineInputArraySchema) isCommandlineInputArraySchemaType()  {}
func (_ CommandlineInputEnumSchema) isCommandlineInputArraySchemaType()   {}

type CommandlineInputArraySchema struct {
	Items        CommandlineInputArraySchemaType
	Type         string // MUST be array
	Label        *string
	Doc          []string
	Name         *string
	InputBinding *CommandlineBinding
}

type CommandlineInputEnumSchema struct {
	Symbols      []string
	Type         string // MUST BE enum, only a placeholder for type verification purposes
	Label        *string
	Doc          []string
	Name         *string
	InputBinding *CommandlineBinding
}

type CommandlineInputRecordSchema struct {
	Type         string // MUST BE "record"
	Fields       []CommandlineInputRecordField
	Label        *string
	Doc          *[]string
	Name         *string
	inputBinding *CommandlineBinding
}

type CommandlineInputParameterType interface {
	isCLIParamType()
}

func (_ CWLNull) isCLIParamType()                      {}
func (_ CWLBool) isCLIParamType()                      {}
func (_ CWLInt) isCLIParamType()                       {}
func (_ CWLLong) isCLIParamType()                      {}
func (_ CWLFloat) isCLIParamType()                     {}
func (_ CWLDouble) isCLIParamType()                    {}
func (_ CWLString) isCLIParamType()                    {}
func (_ CWLFile) isCLIParamType()                      {}
func (_ CWLDirectory) isCLIParamType()                 {}
func (_ CWLStdin) isCLIParamType()                     {}
func (_ CommandlineInputRecordSchema) isCLIParamType() {}
func (_ CommandlineInputEnumSchema) isCLIParamType()   {}
func (_ CommandlineInputArraySchema) isCLIParamType()  {}
func (_ String) isCLIParamType()                       {}

type CommandlineBinding struct {
	LoadContents  *bool
	Position      *int
	Prefix        *string
	Seperate      *bool
	ItemSeperator *string
	ValueFrom     CWLExpressionString
	ShellQuote    *bool
}

type CommandlineInputParameter struct {
	Type           []CommandlineInputParameterType // len(1) == scalar while len > 1 == array
	Label          *string
	SecondaryFiles []CWLSecondaryFileSchema // len(1) == scalar while len > 1 == array
	Streamable     *bool
	Doc            []string
	Id             *string
	Format         CWLFormat
	LoadContents   *bool
	LoadListing    LoadListingEnum
	Default        interface{}
	InputBinding   *CommandlineBinding
}

type CommandlineOutputBindingGlob interface {
	isCommandlineOutputBindingGlob()
}

func (_ String) isCommandlineOutputBindingGlob()        {}
func (_ Strings) isCommandlineOutputBindingGlob()       {}
func (_ CWLExpression) isCommandlineOutputBindingGlob() {}

type CommandlineOutputBinding struct {
	LoadContents *bool
	LoadListing  LoadListingEnum
	Glob         CommandlineOutputBindingGlob
	OutputEval   CWLExpression
}

type CommandlineOutputParameterType interface {
	isCommandlineOutputParameterType()
}

type CommandlineOutputParameter struct {
	Type           []CommandlineOutputParameterType
	Label          *string
	SecondaryFiles []CWLSecondaryFileSchema
	Streamable     *bool
	Doc            []string
	Id             *string
	Format         CWLFormat
	OutputBinding  *CommandlineOutputBinding
}

type CommandlineArgument interface {
	isCommandlineArguement()
}

func (_ String) isCommandlineArguement()             {}
func (_ CWLExpression) isCommandlineArguement()      {}
func (_ CommandlineBinding) isCommandlineArguement() {}

type CommandlineTool struct {
	Inputs       []CommandlineInputParameter
	Outputs      []CommandlineOutputParameter
	Class        string // Must be "CommandLineTool"
	Id           *string
	Label        *string
	Doc          []string
	Requirements []CWLRequirements
	Hints        []interface{}
	CWLVersion   *string
	Intent       []string
	BaseCommand  []string
	Arguments    []CommandlineArgument
	Stdin        CWLExpressionString
	Stderr       CWLExpressionString
	Stdout       CWLExpressionString
}
